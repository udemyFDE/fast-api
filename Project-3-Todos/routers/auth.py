'''

import APIRouter from fastapi which will allow us to be able to route from main.py file to auth.py

in main.py import this auth.py to use this router
'''

from fastapi import APIRouter
from pydantic import BaseModel
from database.models import Users
from passlib.context import CryptContext
from sqlalchemy.util import deprecated

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

# use the same variable used for APIRouter(), instead of @app.get --> @router.get

# Create user (POST)
@router.post("/auth")

# need to import the Users model from models.py
async def create_user(create_user_request: CreateUserRequest):

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

    return create_user_model


# Fetch/Read the user (GET)
# @router.get("/auth/")
#
# async def get_user():
#     return {"user": "Authenticated"}