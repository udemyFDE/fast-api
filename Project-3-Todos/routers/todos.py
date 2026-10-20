'''

This file is the root of application endpoints
Has the same content of main-before-routers.py
remove app = FastAPI() and add router = APIRouter()
replace @app with @router

import this todos.py in main.py
'''

from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from pydantic import BaseModel, Field
from starlette import status

# import models # if models.py is in the same folder as of main.py
from database import models
from database.models import Todos
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from .auth import get_current_user

router = APIRouter()

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

# Pydantic model to validate the POST/PUT requests
class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=25)
    description: str = Field(min_length=1, max_length=100)
    priority: int = Field(ge=1, le=5)
    complete: bool
    # didn't add the ID as it is defined as a primary key and index in the models.py
    # the DB will take care of the ID to increment automatically for each create request
    # sql alchemy will take care of this.

# read all the records in the DB (GET)
@router.get("/", status_code=status.HTTP_200_OK)

async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    # return db.query(Todos).all()
    # Todos need to be imported from models.py, which has the Todos Class defined
    # the app will run the select * from todos query
    # get_todos = db.query(Todos).all()
    get_todos = db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
    # if get_todos is not None:
    if get_todos:
        return get_todos
    raise HTTPException(
        status_code=404,
        detail=f"No data found for the user '{user.get('username')}'"
    )

# Get a record (GET) using the ID as path parameter

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)

async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    # todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    # todo_model = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.get('id')).first()
    todo_model = (db.query(Todos).filter(Todos.id == todo_id).
                  filter(Todos.owner_id == user.get('id')).first())
    if todo_model is not None:
        return todo_model
    raise HTTPException(
        status_code=404,
        detail=f"No record found with Id: '{todo_id}' for the user '{user.get('username')}'"
    )

# Create a record (POST)

@router.post("/todo", status_code=status.HTTP_201_CREATED)

async def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    # todo_model = Todos(**todo_request.model_dump())
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))
    # here the 'id' in get should be the same key that is used to return
    # from get_current_user in auth.py
    db.add(todo_model)
    db.commit()


# Update a record (PUT) using the ID as path parameter

@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def read_todo(user: user_dependency, db: db_dependency,
                    todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    todo_model = (db.query(Todos).filter(Todos.id == todo_id).
                  filter(Todos.owner_id == user.get('id')).first())

    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No record found with the Id `{todo_id}` for user '{user.get('username')}'"
        )

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    # this will make sure the sql alchemy knows the same record fetched above is updated
    # and not create a new record or a duplicate

    db.add(todo_model)
    db.commit()


# Delete a record (DELETE) using the ID as path parameter

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    todo_model = (db.query(Todos).filter(Todos.id == todo_id).
                  filter(Todos.owner_id == user.get('id')).first())

    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No record found with the Id `{todo_id}` for user '{user.get('username')}'"
        )

    # db.query(Todos).filter(Todos.id == todo_id).delete()
    db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()
    db.commit()