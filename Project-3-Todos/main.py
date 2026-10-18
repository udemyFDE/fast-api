'''

This is the main file where we have the application

import the models (name of the file, here we used models.py) which we use to define the table

import the engine (variable name for create_engine() in database.py) from database
'''

from fastapi import FastAPI
from database import models
from database.database import engine
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# this will run only if todos.db do not exist
# if the db is already create, it will use the same one

# router for Auth is imported and used
# this will run the APIs from auth.py with main.py
app.include_router(auth.router)

app.include_router(todos.router)

# Instead of creating api endpoints for app, we have the api endpoints from routers