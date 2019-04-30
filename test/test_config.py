import sys
sys.path.append('../motion-sensor')

import motionsensor.config as config

PROPS_FILE = "test/resources/props.json"

EXPECTED_USERNAME = "Adrian"
EXPECTED_IMAGE_LIST = [
    "adrian.jpg", 
    "adrian2.jpg"
]

EXPECTED_IMAGE_FOLDER_LOCATION = "images"

def test_open_config_file():
    conf = config.Config(PROPS_FILE)
    assert conf is not None

def test_contains_user():
    conf = config.Config(PROPS_FILE)

    result = False
    for user in conf.get_users():
        if user.get_username() == EXPECTED_USERNAME and sorted(user.get_files_list()) == sorted(EXPECTED_IMAGE_LIST):
            result = True

    assert result == True

def test_is_user_present_in_config():
    conf = config.Config(PROPS_FILE)
    assert conf.get_image_folder_location() == EXPECTED_IMAGE_FOLDER_LOCATION
