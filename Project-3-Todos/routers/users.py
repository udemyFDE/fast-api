'''

1. Create a new route called Users.

2. Then create 2 new API Endpoints

get_user: this endpoint should return all information about the user that is currently logged in.

change_password: this endpoint should allow a user to change their current password.

import this file to main.py and add the router in there
'''

from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter, Form
from pydantic import BaseModel, Field, SecretStr
from pygments.lexer import default
from starlette import status

# import models # if models.py is in the same folder as of main.py
from database import models
from database.models import Todos, Users
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from .auth import get_current_user
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=['user']
    # divide our application with a new title of auth that will show all the auth APIs
    # and then each API endpoint within this auth,py file is going to start with '/user'.
)

def get_db():
    db = SessionLocal() # SessionLocal need to be imported from database.py
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
# Annotated is imported from typing
# Session is imported from sqlalchemy.orm
# Depends is imported from fastapi

# use this as a dependency to validate the user first
# Having this dependency for the endpoint requires the token to be passed by user
# before sending any request/accessing the endpoint
user_dependency = Annotated[dict, Depends(get_current_user)]

# we can create the bcrypt context and use it
# this is same from auth.py
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


###################
# Pydantic model to validate the GET/PUT requests for Users
###################
# # as normal strings
class UserVerification(BaseModel):
    current_password: str
    new_password: str = Field(min_length=6)


# # as form data and secure string, just for understanding
# class ChangePasswordForm:
#     def __init__(
#         self,
#         current_password: Annotated[SecretStr, Form()],
#         new_password: Annotated[SecretStr, Form(min_length=6)],
#         confirm_password: Annotated[SecretStr, Form(min_length=6)]
#     ):
#         self.current_password = current_password
#         self.new_password = new_password
#         self.confirm_password = confirm_password


# GET record of current user
@router.get("/", status_code=status.HTTP_200_OK)

async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not Authorized")
    return db.query(Users).filter(Users.id == user.get('id')).first()


# Update (PUT) the password of current user
@router.put("/change_password", status_code=status.HTTP_204_NO_CONTENT)

# passwords as normal string
async def change_user_password(user: user_dependency, db: db_dependency,
                               user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Not Authorized")

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.current_password, user_model.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Password change failed. Please enter your current password correctly to proceed"
        )

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)

    db.add(user_model)
    db.commit()

# # passwords as secure string
# async def change_password(user: user_dependency, db: db_dependency,
#                           form_data: Annotated[ChangePasswordForm, Depends()]):
#     if user is None:
#         raise HTTPException(status_code=401, detail="Not Authorized")
#
#     if form_data.new_password.get_secret_value() != form_data.confirm_password.get_secret_value():
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="New password and confirm password do not match."
#         )
#
#     user_model = db.query(Users).filter(Users.id == user.get('id')).first()
#
#     if not bcrypt_context.verify(form_data.current_password.get_secret_value(), user_model.hashed_password):
#         raise HTTPException(
#             status_code=401,
#             detail="Password change failed. Please enter your current password correctly to proceed"
#         )
#
#     user_model.hashed_password = bcrypt_context.hash(form_data.new_password.get_secret_value())
#
#     db.add(user_model)
#     db.commit()
