'''

this is to test todos.py in routers folder

'''
from http.client import responses

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database.database import Base
from main import app
from routers.todos import get_db, get_current_user

# to force our application to be run as test
from fastapi.testclient import TestClient
from fastapi import status

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
    return {'username': 'adminhyd', 'id': 2, 'role': 'admin'}
    # these user details are of the existing user in the users table of prod db todosapp.db



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


# a test function

def test_read_all_authenticated():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

# Only with this function, this file will create a testdb.db which would be empty
# the test will pass if, in todos.py, read_all function only has the return statement below
# return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
# instead of the below logic for exception
#  # get_todos = db.query(Todos).filter(Todos.owner_id == user.get('id')).all()
#     # if get_todos:
#     #     return get_todos
#     # raise HTTPException(
#     #     status_code=404,
#     #     detail=f"No data found for the user '{user.get('username')}'"
#     # )