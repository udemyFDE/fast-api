'''

assert --> is how you validate some type of data compared to another piece of data.

'''

def test_equal_or_not_equal():
    assert 3 == 3   # true
    assert 3 != 1   # true
    # assert 3 != 3   # false
    # assert 3 == 2   # false
    # having multiple assertions in the same function
    # will see the failed error for the assertions that do not pass


