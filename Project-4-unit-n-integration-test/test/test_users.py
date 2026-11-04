'''

This is to test the routers/users.py

As we now have utils.py, import it here

Users test also should be done for user's todos, so we need to add a fixture for this in utils.py

need to import these in utils.py
from database.models import Users
from routers.auth import bcrypt_context

'''

from .utils import *
from routers.users import get_db, get_current_user
from fastapi import status



# # now we need to add app dependency overrides
# # in users.py, we have a DB dependency --> db_dependency = Annotated[Session, Depends(get_db)]
# # to override the calls for get_db with override_get_db when running tests to use test db
# # this requires to import app from main.py
app.dependency_overrides[get_db] = override_get_db


# # In users.py we also have user dependency --> user_dependency = Annotated[dict, Depends(get_current_user)]
# # it calls get_current_user from routers/auth.py file
# # when a user is authenticated, we need to mock/fake that user whenever that dependency is called
# # need to override this user dependency as well
app.dependency_overrides[get_current_user] = override_get_current_user


### Test functions ####

# this is to test the Get request get_user get("/user") in users.py
def test_get_user(test_user):
    response = client.get("/user")
    # prefix="/user", and endpoint is /user in users.py
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'testuser'
    assert response.json()['email'] == 'testuser@example.com'
    assert response.json()['first_name'] == 'test'
    assert response.json()['last_name'] == 'user'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(91)-9123-456-789'
    # this data should be same as provided in test_user fixture in utils.py



# this is to test the Get request change_user_password put("/user/change_password") in users.py
def test_change_user_password(test_user):
    response = client.put("/user/change_password", json={"current_password": "testpassword",
                                                         "new_password": "newtestpassword"})
    # json keys are the same as defined for class 'UserVerification' in users.py
    # value for current_password must be same as provided for hashed_password in test_user fixture in utils.py
    # prefix="/user", and endpoint is /user in users.py
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_user_password_invalid_current_password(test_user):
    response = client.put("/user/change_password", json={"current_password": "wrongpassword",
                                                         "new_password": "newtestpassword"})
    # json keys are the same as defined for class 'UserVerification' in users.py
    # value for current_password must be different than provided for hashed_password in test_user fixture in utils.py
    # prefix="/user", and endpoint is /user/change_password in users.py
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Password change failed. Please enter your current password correctly to proceed'}
    # the json detail should be same as the one for HTTPException in bcrypt_context.verify
    # for change_user_password in users.py



# this is to test the Get request update_phone_number put("/user/update/{phone_number}") in users.py
def test_update_phone_number(test_user):
    response = client.put("/user/update/(91)-9123-123-456")
    # prefix="/user", and endpoint is /user/change_password in users.py
    assert response.status_code == status.HTTP_204_NO_CONTENT


# # test function without using the fixture
# def test_get_user():
#     response = client.get("/user")
#     # prefix="/user", and endpoint is /user in users.py
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() is None