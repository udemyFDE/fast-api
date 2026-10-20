'''

This file is to have the endpoints that are allowed only for Admin users

import this admin.py in main.py and add the router of this file for the app in main.app
'''

from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from pydantic import BaseModel, Field
from pygments.lexer import default
from starlette import status

# import models # if models.py is in the same folder as of main.py
from database import models
from database.models import Todos
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from .auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=['admin']
    # divide our application with a new title of auth that will show all the auth APIs
    # and then each API endpoint within this auth,py file is going to start with '/admin'.
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


# GET all records of all users as an Admin user
@router.get("/todo", status_code=status.HTTP_200_OK)

async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('role').lower() != 'admin':
        # role in get should be the same key used in get_current_user function in auth.py
        raise HTTPException(status_code=401, detail="Not Authorized")
    return db.query(Todos).all()

# DELETE any record as an Admin user

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('role').lower() != 'admin':
        # role in get should be the same key used in get_current_user function in auth.py
        raise HTTPException(status_code=401, detail="Not Authorized")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No record found with the Id `{todo_id}`"
        )

    # db.query(Todos).filter(Todos.id == todo_id).delete()
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()


