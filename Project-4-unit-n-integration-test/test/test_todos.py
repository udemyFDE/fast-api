'''

this is to test todos.py in routers folder

'''
from http.client import responses

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database.database import Base
from main import app
from routers.todos import get_db, get_current_user

# to force our application to be run as test
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from database.models import Todos

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
    return {'username': 'adminhyd', 'id': 1, 'role': 'admin'}
    # these user details can be anything, no need to exist in prod DB



# # now we need to add app dependency overrides
# # in todos.py, we have a DB dependency --> db_dependency = Annotated[Session, Depends(get_db)]
# # to override the calls for get_db with override_get_db when running tests to use test db
# # this requires to import app from main.py
app.dependency_overrides[get_db] = override_get_db


# # In todos.py we also have user dependency --> user_dependency = Annotated[dict, Depends(get_current_user)]
# # it calls get_current_user from routers/auth.py file
# # when a user is authenticated, we need to mock/fake that user whenever that dependency is called
# # need to override this user dependency as well
app.dependency_overrides[get_current_user] = override_get_current_user

# app from main.py
client = TestClient(app)


# fixture
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


# now we can call the fixture by passing the function trest_todo, under it, as an argument
# in the below function, this is to test the read_all endpoint get("/") in todos.py
def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    # above response code should be same as in the original endpoint
    # this is to test read_all, so the return will be a list
    assert response.json() == [{'complete': False, 'title': 'Learn to code',
                                'description': 'Need to learn everyday..!',
                                'priority': 5,
                                'owner_id': 1,
                                'id': 1}]
    # as it is to test GET the data in assert should match the one inserted in test_todo fixture


# this is to test the read_todo get("/todo/{todo_id}") endpoint in todos.py
# here, for testing the todo_id is 1
def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    # above response code should be same as in the original endpoint
    # this is to test read one record, so the return will be a single object
    assert response.json() == {'complete': False, 'title': 'Learn to code',
                                'description': 'Need to learn everyday..!',
                                'priority': 5,
                                'owner_id': 1,
                                'id': 1}


# this is to test for todo not found
#  here, for testing the todo_id is 999
# def test_read_one_authenticated_not_found(test_todo):
def test_read_one_authenticated_not_found():
    response = client.get("/todo/999")
    assert response.status_code == 404
    # above response code should be same as in the original endpoint
    assert response.json() == {'detail': 'Todo not found'}
    # these assertions should match with the HTTP exception for read_todo in todos.py



# this is to test the create request create_todo post("/todo") in todos.py
def test_create_todo(test_todo):
    request_data = {
        'title': 'New Todo',
        'description': 'New Todo description',
        'priority': 5,
        'complete':False
    }
    # this data should satisfy the conditions set for TodoRequest model in todos.py
    # like min and max length, etc.

    response = client.post("/todo", json=request_data)
    assert response.status_code == 201
    # assert response.status_code == status.HTTP_201_CREATED
    # above response code should be same as in the original endpoint

    # this is to check if the data sent through POST API endpoint was actually saved correctly in the test database.
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')
    # here the id is passed as 2, because the id = 1 is used for the record inserted by test_todo fixture
    # this create test is adding another record, so the id should be the next


# this is to test the update request update_todo put("/todo/{todo_id}") in todos.py
# Here we need to update the data already saved in test DB either by GET or POST tests
def test_update_todo(test_todo):
    request_data = {
        'title': 'Updated todo title..!',
        'description': 'New Todo description',
        'priority': 5,
        'complete':False
    }
    # this data should satisfy the conditions set for TodoRequest model in todos.py
    # like min and max length, etc.

    response = client.put("/todo/1", json=request_data)
    assert response.status_code == 204
    # assert response.status_code == status.HTTP_204_NO_CONTENT
    # above response code should be same as in the original endpoint
    # this is to check if the data sent through PUT API endpoint was actually saved correctly in the test database.
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == request_data.get('title')
    # Here we need to use the ID of the data already saved, as this is to test update operation
    # so, used the id = 1 as this will be the only record inserted by fixture in test DB when called by this function


def test_update_todo_not_found(test_todo):
    request_data = {
        'title': 'Updated todo title..!',
        'description': 'New Todo description',
        'priority': 5,
        'complete':False
    }
    # this data should satisfy the conditions set for TodoRequest model in todos.py
    # like min and max length, etc.

    response = client.put("/todo/999", json=request_data)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}
    # above response code should be same as in the original endpoint
    # these assertions should match with the HTTP exception for read_todo in todos.py




# # test function
# # returns nothing as there is no data in test database.
# # When this test is ran, we add an item to test database.
# # We can then read to make sure that the API endpoint is working as expected, and then we want
# # the test to automatically delete the todos inside the database on runtime.
# # So when a test is ran for every single function, we want to add the todo and run whatever operation we need
# # to run on it, and then delete everything from the test database before the next test ran
# # we need to create a fixture which can be created that happens before the function is called.
# # to use fixture, we need to import `pytest' and 'Todos', the class object for todos table, from models.py


# # test function without using the fixture
# def test_read_all_authenticated():
#     response = client.get("/")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == []

# # Only with this function, this file will create a testdb.db which would be empty
# # the test will pass if, in todos.py, read_all function only has the return statement below
# # return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
# # instead of the below logic for exception
#  # get_todos = db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
#     # if get_todos:
#     #     return get_todos
#     # raise HTTPException(
#     #     status_code=404,
#     #     detail=f"No data found for the user '{user.get('username')}'"
#     # )