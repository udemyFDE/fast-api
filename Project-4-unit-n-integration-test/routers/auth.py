'''

import APIRouter from fastapi which will allow us to be able to route from main.py file to auth.py

in main.py import this auth.py to use this router
'''

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database.models import Users
from database.database import engine, SessionLocal
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.util import deprecated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone

# Instead of app = FastAPI(), we have this
router = APIRouter(
    prefix="/auth",
    tags=['auth']
    # divide our application with a new title of auth that will show all the auth APIs
    # and then each API endpoint within this auth,py file is going to start with '/auth'.
)

# JWT require a secret and algorithm, both will work together to add a signature for JWT
# and ensure the JWT is secure and authorized
# for secret can use this command --> python -c "import secrets; print(secrets.token_hex(32))"
# OR --> openssl rand -hex 32
SECRET_KEY = 'bede58bf90067cf4c4cc693df5c99804ed0bf08ce43949ea32b4925bdc5c1beb'
ALGORITHM = 'HS256'


# we can create the bcrypt context and use it
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# token context which has the URL that the client will send to the application
# need this to verify the token as a dependency in api request
# Used this as dependency in the function to verify the user
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

# without '/auth' prefix, can use this
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str  # in Users model it is defined as hashed_password
    role: str
    phone_number: str
    # Id is not added here, as SQLAlchemy will take care of incrementing the IDs for every user being added
    # and is_active has the default set to True in the table definition in model.py

# This class is to get more infor about the token after authentication
class Token(BaseModel):
    access_token: str
    token_type: str


# function to connect to the DB
def get_db():
    db = SessionLocal() # SessionLocal need to be imported from database.py
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# function to authenticate the user
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False # if the user is not found
    if not bcrypt_context.verify(password, user.hashed_password):
        # hash the provided password and compare with the hashed password in database
        # return false if password do not match
        return False
    # return True
    return user

# function to create access token for JWT
# need to import timedelta, datetime and timezone from datetime
# added the role to allow certain endpoints to work only for admin users
# In the users table we also added a column for role in model.py to be passed while creating the user
def create_access_token(username: str, user_id: int, role: str, expires_delta=timedelta):
    encoded_value = {'sub': username, 'id': user_id, 'role': role}
    # expires = datetime.utcnow() # deprecated
    expires = datetime.now(timezone.utc) + expires_delta
    encoded_value.update({'exp': expires})
    return jwt.encode(encoded_value, SECRET_KEY, algorithm=ALGORITHM)


# Function to verify the user by decoding the token
# for each request in the future that needs security
# We will call this get_current_user first to verify the token that's getting passed in as the
# OAuth2 bearer token in our client call.
# need to import this function to todos.py file for the application
# add the Depends() for 'oauth2_bearer', otherwise the lock icon will not be visible in swagger
# If no Depends() for 'oauth2_bearer' is used, we see a field to enter the token which will be passed
# as a query parameter and will fail
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate the user"
            )

        return {"username": username, "id": user_id, "role": user_role}
        # when referring this function, need to use the same keys declared in 'return' above

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate the user"
        )



# use the same variable used for APIRouter(), instead of @app.get --> @router.get

#######################
# Creating a new user #
#######################

# Create user (POST)
# @router.post("/auth", status_code=status.HTTP_201_CREATED)
# As we added a prefix '/auth' in router if we use it here again the endpoint will be '/auth/auth'
# so we just keep '/' for this endpoint as the prefix is same

@router.post("/", status_code=status.HTTP_201_CREATED)
# need to import the Users model from models.py
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):

    # This will not work as the 'create_user_request' has password whereas Users model has hashed_password
    # create_user_model = Users(**create_user_request.model_dump())

    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        phone_number=create_user_request.phone_number,
        is_active=True
    )

    # return create_user_model
    db.add(create_user_model)
    db.commit()


##########################
# Authentication of user #
##########################

# Get a token
@router.post("/token", response_model=Token)

async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        # return "Failed Authentication"
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate the user `{form_data.username}`"
        )
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    # return "Successful Authentication"
    # return token
    return {'access_token': token, 'token_type': 'bearer'}
