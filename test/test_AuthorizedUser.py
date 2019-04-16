import sys
sys.path.append('/mnt/data/Workspace/motion-sensor')

from motionsensor.AuthorizedUser import AuthorizedUser

TESTNAME = "Adrian"
FILES_LIST = [
    'qwe.png',
    'abc.png',
    'image.png'
]

def test_createUser():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert user != None

def test_returnUsername():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert user.get_username() == TESTNAME

def test_returnFilesList():
    user = AuthorizedUser(TESTNAME, FILES_LIST)
    assert sorted(user.get_file_list()) == sorted(FILES_LIST)