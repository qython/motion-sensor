import motionsensor.config as config
import os

PROPS_FILE = os.path.join(os.path.dirname(__file__), "resources/props.json")

EXPECTED_USERNAME = "Adrian"
EXPECTED_IMAGE_LIST = [
    "adrian.jpg", 
    "adrian2.jpg"
]
EXPECTED_IMAGE_FOLDER_LOCATION = "test/resources/images"

EXPECTED_TRIES = 3
EXPECTED_INTERVAL = 1
EXPECTED_TRESHOLD_WEIGHT = 1
EXPECTED_DRIFT_WEIGHT = 10
EXPECTED_MOVE_MIN = 1000
EXPECTED_MOVE_MAX = 3000

EXPECTED_IP_CAM_ADDR = "http://192.168.0.13:8080"
EXPECTED_MAX_MEASUREMENTS = 40
EXPECTED_LAST_PHOTO_FILE_NAME = "last_photo.jpg"
EXPECTED_PHOTO_ENDPOINT = "shot.jpg"
EXPECTED_TMP_FOLDER_LOCATION = "tmp"
EXPECTED_SENSOR_DATA_ENDPOINT = "sensors.json?sense=motion"

def test_open_config_file():
    conf = config.load_config(PROPS_FILE)
    assert conf is not None

def test_face_recognition_config():
    conf = config.load_config(PROPS_FILE)
    recognition_config = conf.get_face_recognition_config()

    result = False
    for user in recognition_config.users:
        if user.get_username() == EXPECTED_USERNAME and sorted(user.get_files_list()) == sorted(EXPECTED_IMAGE_LIST):
            result = True

    assert result == True
    assert recognition_config.image_folder_location == EXPECTED_IMAGE_FOLDER_LOCATION

def test_motion_config():
    conf = config.load_config(PROPS_FILE)
    motion_config = conf.get_motion_config()

    assert motion_config is not None
    assert motion_config.move_max == EXPECTED_MOVE_MAX
    assert motion_config.move_min == EXPECTED_MOVE_MIN
    assert motion_config.treshold_weight == EXPECTED_TRESHOLD_WEIGHT
    assert motion_config.tries == EXPECTED_TRIES
    assert motion_config.interval == EXPECTED_INTERVAL
    assert motion_config.drift_weight == EXPECTED_DRIFT_WEIGHT

def test_android_connector_config():
    conf = config.load_config(PROPS_FILE)
    connector_config = conf.get_android_connector_config()
    assert connector_config is not None
    assert connector_config.ip_cam_addr == EXPECTED_IP_CAM_ADDR
    assert connector_config.last_photo_file_name == EXPECTED_LAST_PHOTO_FILE_NAME
    assert connector_config.max_measurements == EXPECTED_MAX_MEASUREMENTS
    assert connector_config.photo_endpoint == EXPECTED_PHOTO_ENDPOINT
    assert connector_config.sensor_data_endpoint == EXPECTED_SENSOR_DATA_ENDPOINT
    assert connector_config.tmp_folder_location == EXPECTED_TMP_FOLDER_LOCATION