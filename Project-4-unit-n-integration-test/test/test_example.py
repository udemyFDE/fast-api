'''

assert --> is how you validate some type of data compared to another piece of data.

'''

import pytest

# Validate integers
def test_equal_or_not_equal():
    assert 3 == 3   # true
    assert 3 != 1   # true
    # assert 3 != 3   # false
    # assert 3 == 2   # false
    # having multiple assertions in the same function
    # will see the failed error for the assertions that do not pass

# validate instances
def test_is_instance():
    assert isinstance('this is a string', str)  # return true
    assert not isinstance('10', int)    # False --> return true because of not
    assert isinstance(10, int)  # return true


# validate boolean
def test_boolean():
    validated = True
    assert validated is True    # return true, as validated (variable) is set as true above
    assert ('Hello' == 'World') is False    # return true, as both strings are not same

# validate type
def test_type():
    assert type('Hello' is str)     # return true
    assert type('World' is not int) # return true


# validate > & <
def test_greater_and_less_than():
    assert 7 > 3    # return true
    assert 4 < 10   # return true


# validate list
def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list        # return true
    assert 7 not in num_list    # return true
    assert all(num_list)        # return true
    assert not any(any_list)    # return true, as any_list has all False

##########################
## PyTest using Objects ##
##########################
# # need to import pytest, this will allow to use others than assert

class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

# # To use pytest fixture, need to import pytest
@pytest.fixture()
def default_employee():
    return Student('John', 'Doe', 'Computer Science', 3)
# # default_employee is a function and is a pytest fixture


# # this will call the pytest fixture function default_employee which return the object
# # can use that object inside our test.
# # So that's a way for us to be able to reuse creating a student or
# # reuse creating any kind of object in
def test_person_initialization(default_employee):
    assert default_employee.first_name == 'John', 'First name should be John'  # second part is a message
    assert default_employee.last_name == 'Doe', 'Last name should be Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3

# # we are instantiating a new object in the test, and we have to do
# # this every single time if we want to be able to use the values of that object.
# # assume that there's going to be more tests for that object.
# # And we don't want to have to instantiate a new object every
# # single time we're going to test against it.
# # And that's where Pytest fixtures come into play.
# # And pytest fixtures will allow us to be able to instantiate
# # an object and then pass it into our test functionality
# # This all happens automatically behind the scenes, and it allows us to kind of add some dependencies
# # to our test, which will allow us to create less code.

# def test_person_initialization():
#     p = Student('John', 'Doe', 'Computer Science', 3)
#     assert p.first_name == 'John', 'First name should be John'  # second part is a message
#     assert p.last_name == 'Doe', 'Last name should be Doe'
#     assert p.major == 'Computer Science'
#     assert p.years == 3