'''

This is the main file where we have the application

import the models (name of the file, here we used models.py) which we use to define the table

import the engine (variable name for create_engine() in database.py) from database

For testing this using pytest, created a file 'test_main.py' under the test folder

'''

from fastapi import FastAPI
# from database import models
from database.models import Base
from database.database import engine
from routers import auth, todos, admin, users

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)
# # if we import models completely

Base.metadata.create_all(bind=engine)
# # if we import only Base from models
# this will run only if todos.db do not exist
# if the db is already create, it will use the same one


# # simple route to check if the application is up and running.
# # Now this is typically called a health check.
@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


# router for Auth is imported and used
# this will run the APIs from auth.py with main.py
app.include_router(auth.router)

app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

# Instead of creating api endpoints for app, we have the api endpoints from routers