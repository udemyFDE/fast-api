'''

This is the main file where we have the application

import the models (name of the file, here we used models.py) which we use to define the table

import the engine (variable name for create_engine() in database.py) from database
'''

from fastapi import FastAPI
from database import models
# import models # if models.py is in the same folder as of main.py
from database.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)