'''

This is the main file where we have the application

import the models (name of the file, here we used models.py) which we use to define the table

import the engine (variable name for create_engine() in database.py) from database
'''

from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status

# import models # if models.py is in the same folder as of main.py
from database import models
from database.models import Todos
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# this will run only if todos.db do not exist
# if the db is already create, it will use the same one



'''
# yield means only the code prior to and including the yield statement is executed before sending
# a response. The code following the yield statement is executed after the response has been delivered.
# Now this makes fast API quicker because we can fetch information from a database, return it to the
# client and then close off the connection to the database after.
'''
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
@app.get("/", status_code=status.HTTP_200_OK)

async def read_all(db: db_dependency):

    # return db.query(Todos).all()
    # Todos need to be imported from models.py, which has the Todos Class defined
    # the app will run the select * from todos query

    get_todos = db.query(Todos).all()
    if get_todos is not None:
        return get_todos
    raise HTTPException(
        status_code=404,
        detail={"No data found"}
    )

# Get a record (GET) using the ID as path parameter

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)

async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(
        status_code=404,
        detail=f"No record found with Id: {todo_id}"
    )

# Create a record (POST)

@app.post("/todo", status_code=status.HTTP_201_CREATED)

async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


# Update a record (PUT) using the ID as path parameter

@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def read_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No record found with the Id: {todo_id}"
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

@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)

async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No record found with the Id: {todo_id}"
        )

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()