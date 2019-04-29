import sys
sys.path.append('../motion-sensor')

from motionsensor.authorized_user import AuthorizedUser

TESTNAME = "Adrian"
FILES_LIST = [
    'qwe.png',
    'abc.png',
    'adrian.png'
]

def test_create_user():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert user != None

def test_return_username():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert user.get_username() == TESTNAME

def test_return_files_list():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert sorted(user.get_files_list()) == sorted(FILES_LIST)