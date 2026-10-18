'''
models is a way for SQL alchemy to be able to understand what kind of database tables we are going
to be creating within our database in the future.

Now a database model is going to be the actual record that is inside a database table.

first thing we need to import is inside our database.py
We created a Base from our declarative_base and we want to import that into our models.
And that just means that we are going to be creating this model for our database.py file.
'''
from math import trunc

from .database import Base
# from database import Base # if database.py, models.py and main.py are is same folder
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'
    # this is just a way for SQL alchemy to know what to name this table inside our database later on.

    # columns for the table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)   # 0 = False, 1 = True in a Database
    # ID is going to be a new column within our table and it's going to be an integer.
    # We then want to say primary key equals true because our ID is going to be the primary key, which is
    # a unique ID or the unique identifier for each record.
    # And then let's also just say index equals true and index is just a way for us to be able to increase
    # performance by telling our database table that this is indexable, which means it's going to be unique.