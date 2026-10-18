
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

# Get the directory containing database.py
# for this we need to import Path from pathlib
BASE_DIR = Path(__file__).resolve().parent

# this URL is going to be used to be able to create a location of this database on our fast API application.
# that our database is going to be inside our project-3 folder.
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# Create the database inside the Database folder
# database is going to be inside the project-3/database/
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR / 'todos.db'}"

# related info below # create_engine #
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# related info below # create a session local #
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# related info below # create a database #
Base = declarative_base()

#################
# create_engine #
#################
'''
The next thing we need is to be able to create an engine for our application.
And now a database engine is something that we can use to be able to open up a connection and be able
to use our database.
import create_engine from SQL Alchemy

the connect arguments are arguments that we can pass into our create engine, which will allow
us to be able to define some kind of connection to a database.

Set check_same_thread to false.
By default, SQLite will only allow one thread to communicate with it.
Assuming that each thread will handle an independent request.
This is to prevent any kind of accident sharing of the same connection for different kind of requests.
But in fast API it's very normal to have more than one thread that could interact with the database
at the same time.
'''

#################
# session local #
#################
'''
need to create a session local and each instance of the session local will have a database session.
The class itself is not a database session yet.
we just need to be able to create an instance of session local that will be able to become
an actual database in the future.

import sessionmaker from SQLAlchemy.ORM 

autocommit equals false.

Autoflush equals false.

And bind equals engine.

we want the session local, which we're going to be using in our application.
You'll see when we use session local, we want to bind to the engine that we just created and we want
to make sure that our auto commits and auto flushes are false or the database transactions are going
to try and do something automatically.

And we want to be fully control of everything our database will do in the future.
'''


#####################
# database creation #
#####################
'''
the last thing we need to do is make sure that we can create a database object that we can then
interact with later on.

import declarative_base from from SQL alchemy.ext.declarative.


Base = declarative_base()

later on, we want to be able to call our database.py file, be able to
create a base which is an object of the database which is going to be able to then control our database.

What this really just means is we're going to be creating database tables and 
then here in our database.py we're going to be able to create an object of our database 
which will then be able to interact with the tables that we create in the future.

'''