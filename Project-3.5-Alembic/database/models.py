'''
models is a way for SQL alchemy to be able to understand what kind of database tables we are going
to be creating within our database in the future.

Now a database model is going to be the actual record that is inside a database table.

first thing we need to import is inside our database.py
We created a Base from our declarative_base and we want to import that into our models.
And that just means that we are going to be creating this model for our database.py file.
'''

# as database.py is inside the database folder which also has model.py
# main.py is outside th database folder, to import Base into models.py from database.py
# so need to use .database as it explicitly pick the database.py
from .database import Base
# from database import Base # if database.py, models.py and main.py are is same folder
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    # phone_number = Column(String)

class Todos(Base):
    __tablename__ = 'todos'
    # this is just a way for SQL alchemy to know what to name this table inside our database later on.

    # columns for the table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)   # 0 = False, 1 = True in a Database
    owner_id = Column(Integer, ForeignKey("users.id")) # to reference the user ID to todos
    # ID is going to be a new column within our table and it's going to be an integer.
    # We then want to say primary key equals true because our ID is going to be the primary key, which is
    # a unique ID or the unique identifier for each record.
    # And then let's also just say index equals true and index is just a way for us to be able to increase
    # performance by telling our database table that this is indexable, which means it's going to be unique.