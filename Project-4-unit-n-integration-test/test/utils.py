'''

Have all the reusable code in this file

'''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database.database import Base
from main import app
from fastapi.testclient import TestClient # to force our application to be run as test
import pytest
from database.models import Todos, Users
from routers.auth import bcrypt_context



# create a test DB in database folder
SQLALCHEMY_DATABASE_URL = 'sqlite:///./database/testdb.db'


# create an engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool
)

# create a testing session local for a testing environment to isolate from prod app
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Calling the engine from database.py file to add Base
# to use table definitions of prod db
Base.metadata.create_all(bind=engine)


# In todos.py we have get_db function to fetch the db details and is added as a dependency for each endpoint
# Now, we need to override the get_db functionality only if we call it from test
# to call the testdb.db instead of production db todosapp.db

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# function to mock the current user
def override_get_current_user():
    return {'username': 'testuser', 'id': 1, 'role': 'admin'}
    # these user details can be anything, no need to exist in prod DB


# app from main.py
client = TestClient(app)


# fixture for todos
@pytest.fixture()

def test_todo():
    # test todo will the todos from model #
    todo = Todos(
        title="Learn to code",
        description="Need to learn everyday..!",
        priority=5,
        complete=False,
        owner_id=1
    )

    # add the data to test DB and delete after test
    db = TestingSessionLocal()  # the session local must be of test DB and not of the prod DB
    db.add(todo)
    db.commit()
    yield todo
    # after yielding the data, it is deleted after every test.... so nothing exist in test DB after test
    # without the below command the data will not be deleted in test DB
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

    # When the fixture is called, it will add the record defined in test_todo
    # when the fixture reaches yield the control will be handed over to the functions calling it
    # once the function is tested, the control is handed to Fixture continuing after yield
    # Fixture cleanup will start, the delete command will be executed to clean up the test DB



# fixture for users
@pytest.fixture()

def test_user():
    # test user will the Users from model #
    user = Users(
        username="testuser",
        email="testuser@example.com",
        first_name='test',
        last_name='user',
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="(91)-9123-456-789"
    )
    # didn't add the id as when this data is inserted in the test DB this will have an id
    # this id will be 1 as we have in the override function above to mock current user

    # add the data to test DB and delete after test
    db = TestingSessionLocal()  # the session local must be of test DB and not of the prod DB
    db.add(user)
    db.commit()
    yield user
    # after yielding the data, it is deleted after every test.... so nothing exist in test DB after test
    # without the below command the data will not be deleted in test DB
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()

    # When the fixture is called, it will add the record defined in test_todo
    # when the fixture reaches yield the control will be handed over to the functions calling it
    # once the function is tested, the control is handed to Fixture continuing after yield
    # Fixture cleanup will start, the delete command will be executed to clean up the test DB