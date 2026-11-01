'''

This is to test the routers/admin.py

As we now have utils.py, import it here

'''

from .utils import *
from routers.admin import get_db, get_current_user
from fastapi import status
from database.models import Todos



# # now we need to add app dependency overrides
# # in admin.py, we have a DB dependency --> db_dependency = Annotated[Session, Depends(get_db)]
# # to override the calls for get_db with override_get_db when running tests to use test db
# # this requires to import app from main.py
app.dependency_overrides[get_db] = override_get_db


# # In admin.py we also have user dependency --> user_dependency = Annotated[dict, Depends(get_current_user)]
# # it calls get_current_user from routers/auth.py file
# # when a user is authenticated, we need to mock/fake that user whenever that dependency is called
# # need to override this user dependency as well
app.dependency_overrides[get_current_user] = override_get_current_user


### Test functions ####

# this is to test the Get request read_all get("/admin/todo") in admin.py
def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    # prefix="/admin", and endpoint is /todo in admin.py
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'complete': False, 'title': 'Learn to code',
                                'description': 'Need to learn everyday..!',
                                'priority': 5,
                                'owner_id': 1,
                                'id': 1}]

    # as this is to test admin, the role in the function to mock the current user
    # def override_get_current_user(): in utils.py is also 'admin'
    # otherwise, this test will fail


# this is to test the delete request delete_todo delete("/admin/todo/{todo_id}") in admin.py
# Here we need to delete the data already saved in test DB that will be inserted by the fixture test_todo
def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == 204
    # assert response.status_code == status.HTTP_204_NO_CONTENT
    # above response code should be same as in the original endpoint
    # this is to check if the data sent through DELETE API endpoint was actually deleted in the test database.
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    # model should be none after deleting the only record inserted by fixture test_todo


def test_admin_delete_todo_not_found(test_todo):
    response = client.delete("/admin/todo/999")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}
    # above response code should be same as in the original endpoint
    # these assertions should match with the HTTP exception for delete_todo in todos.py