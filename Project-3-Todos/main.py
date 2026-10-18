'''

This is the main file where we have the application

import the models (name of the file, here we used models.py) which we use to define the table

import the engine (variable name for create_engine() in database.py) from database
'''

from fastapi import FastAPI, Depends
# import models # if models.py is in the same folder as of main.py
from database import models
from database.models import Todos
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

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


@app.get("/")

async def read_all(db: Annotated[Session, Depends(get_db)]):
    # Annotated is imported from typing
    # Session is imported from sqlalchemy.orm
    # Depends is imported from fastapi
    return db.query(Todos).all()
    # Todos need to be imported from models.py, which has the Todos Class defined