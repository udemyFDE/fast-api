'''

This is to test the routers/auth.py

As we now have utils.py, import it here

'''

from .utils import *
from routers.auth import get_db, authenticate_user
from fastapi import status


# # now we need to add app dependency overrides from utils.py
# # in auth.py, we have a DB dependency --> db_dependency = Annotated[Session, Depends(get_db)]
# # to override the calls for get_db with override_get_db when running tests to use test db
app.dependency_overrides[get_db] = override_get_db