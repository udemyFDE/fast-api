'''

This is to test the routers/auth.py

As we now have utils.py, import it here

'''

from .utils import *
from routers.auth import get_db, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM, get_current_user
from fastapi import status
from jose import jwt
from datetime import timedelta, datetime, timezone
import pytest
from fastapi import HTTPException

# # now we need to add app dependency overrides from utils.py
# # in auth.py, we have a DB dependency --> db_dependency = Annotated[Session, Depends(get_db)]
# # to override the calls for get_db with override_get_db when running tests to use test db
app.dependency_overrides[get_db] = override_get_db


## test functions ##

# this is to test authenticate_user function in auth.py
# which takes (username: str, password: str, db) as input
# here the db will be the test DB and not prod DB as used in auth.py
def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    # db will be the test DB which will be used to test the user authentication

    # this is to test the correct user
    user_authenticated = authenticate_user(test_user.username, 'testpassword', db)
    # the user details are same as provided for test_user fixture in utils.py
    assert user_authenticated is not None
    assert user_authenticated.username == test_user.username

    # this is to test wrong user
    non_existent_user = authenticate_user('wrongusername', 'testpassword', db)
    assert non_existent_user is False

    # this is to test wrong password
    wrong_password_user = authenticate_user(test_user.username, 'wrongpassword', db)
    assert wrong_password_user is False


# this is ot test create_access_token function in auth.py
# which takes (username: str, user_id: int, role: str, expires_delta=timedelta) as input
# Need to import create_access_token, SECRET_KEY, ALGORITHM from auth.py
# import jwt from jose (can refer auth.py), import timedelta from datetime
def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)

    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM],
                               options={'verify_signature': False})

    # the keys in [] should be same as the ones' used for create_access_token encoded in auth.py
    assert decoded_token['sub'] == username
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role


# this is to test get_current_user in auth.py which is defined as async
# and takes (token: Annotated[str, Depends(oauth2_bearer)]) as input
# so the test function also should be defined as async and import get_current_user from auth.py
# need to install pytest-asyncio, import pytest and mark this function as async
@pytest.mark.asyncio
async def test_get_current_user():
    encoded_value = {'sub': 'testuser', 'id': 1, 'role': 'admin'}
    token = jwt.encode(encoded_value, SECRET_KEY, algorithm=ALGORITHM)

    # need to use await as get_current_user is an async function
    user = await get_current_user(token=token)

    assert user == {'username': 'testuser', 'id': 1, 'role': 'admin'}
    # the keys here should match with the ones' used for get_current_user return in auth.py
    # return {"username": username, "id": user_id, "role": user_role}

# this is to test the JWT error
@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encoded_value = {'role': 'user'}
    token = jwt.encode(encoded_value, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)

    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate the user'
    # these should be same as in the HTTPException for



# for the above async test functions, we might get this error, if
# not install pytest-asyncio, import pytest and mark this function as asyncio
# async def functions are not natively supported.
# You need to install a suitable plugin for your async framework, for example:
#   - anyio
#   - pytest-asyncio
#   - pytest-tornasync
#   - pytest-trio
#   - pytest-twisted
#