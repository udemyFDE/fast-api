'''

import APIRouter from fastapi which will allow us to be able to route from main.py file to auth.py

in main.py import this auth.py to use this router
'''

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database.models import Users
from database.database import engine, SessionLocal
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.util import deprecated
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

# Instead of app = FastAPI(), we have this
router = APIRouter()

# we can creat the bcrypt context and use it
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str  # in Users model it is defined as hashed_password
    role: str
    # Id is not added here, as SQLAlchemy will take care of incrementing the IDs for every user being added
    # and is_active has the default set to True in the table definition in model.py


# function to authenticate the user
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False # if the user is not found
    if not bcrypt_context.verify(password, user.hashed_password):
        # hash the provide password and compare with the hashed password in database
        # return false if password do not match
        return False
    return True



# function to connect to the DB
def get_db():
    db = SessionLocal() # SessionLocal need to be imported from database.py
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# use the same variable used for APIRouter(), instead of @app.get --> @router.get

#######################
# Creating a new user #
#######################

# Create user (POST)
@router.post("/auth", status_code=status.HTTP_201_CREATED)

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
        is_active=True
    )

    # return create_user_model
    db.add(create_user_model)
    db.commit()


##########################
# Authentication of user #
##########################

# Get a token
@router.post("/token")

async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    return "Successful Authentication"




# Fetch/Read the user (GET)
# @router.get("/auth/")
#
# async def get_user():
#     return {"user": "Authenticated"}