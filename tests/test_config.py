import motionsensor.config as config
import os

PROPS_FILE = os.path.join(os.path.dirname(__file__), "resources/props.json")

EXPECTED_USERNAME = "Adrian"
EXPECTED_IMAGE_LIST = [
    "adrian.jpg", 
    "adrian2.jpg"
]

EXPECTED_IMAGE_FOLDER_LOCATION = "resources/images"

EXPECTED_IP_CAM_ADDR = "http://192.168.0.13:8080"
EXPECTED_MAX_MEASUREMENTS = 40
EXPECTED_TRIES = 3
EXPECTED_INTERVAL = 1
EXPECTED_TRESHOLD_WEIGHT = 1
EXPECTED_DRIFT_WEIGHT = 10
EXPECTED_MOVE_MIN = 2000
EXPECTED_MOVE_MAX = 10000

def test_open_config_file():
    conf = config.load_config(PROPS_FILE)
    assert conf is not None

def test_contains_user():
    conf = config.load_config(PROPS_FILE)

    result = False
    for user in conf.get_users():
        if user.get_username() == EXPECTED_USERNAME and sorted(user.get_files_list()) == sorted(EXPECTED_IMAGE_LIST):
            result = True

    assert result == True

def test_is_user_present_in_config():
    conf = config.load_config(PROPS_FILE)
    assert conf.get_image_folder_location() == EXPECTED_IMAGE_FOLDER_LOCATION

def test_has_motion_config():
    conf = config.load_config(PROPS_FILE)
    motion_config = conf.get_motion_config()

    assert motion_config is not None
    assert motion_config.ip_cam_addr == EXPECTED_IP_CAM_ADDR
    assert motion_config.max_measurements == EXPECTED_MAX_MEASUREMENTS
    assert motion_config.move_max == EXPECTED_MOVE_MAX
    assert motion_config.move_min == EXPECTED_MOVE_MIN
    assert motion_config.treshold_weight == EXPECTED_TRESHOLD_WEIGHT
    assert motion_config.tries == EXPECTED_TRIES
    assert motion_config.interval == EXPECTED_INTERVAL
    assert motion_config.drift_weight == EXPECTED_DRIFT_WEIGHT