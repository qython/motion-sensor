import json
from os.path import isfile
from motionsensor.authorized_user import AuthorizedUser

USERS_SECTION = "users"
USER_NAME = "name"
USER_IMAGES = "images"

IMAGE_FOLDER = "image_folder_location"

MOTION_SENSOR_SECTION = "motionsensor"

TRIES = "tries"
INTERVAL = "interval"
TRESHOLD_WEIGHT = "treshold_weight"
DRIFT_WEIGHT = "drift_weight"
MOVE_MIN = "move_min"
MOVE_MAX = "move_max"

ANDROID_CONNECTOR_SECTION = "androidconnector"
IP_CAM_ADDRESS = "ip_cam_addr"
MAX_MEASUREMENTS = "max_measurements"
SENSOR_DATA_ENDPOINT = "sensor_data_endpoint"
PHOTO_ENDPOINT = "photo_endpoint"
TMP_FOLDER = "tmp_folder_location"
TMP_FILE_NAME = "last_photo_file_name"

def load_config(file):
    try:
        f = open(file, 'r')
        loaded = json.loads(f.read())
        f.close()
        return Config(loaded)
    except IOError:
        print("ERROR: Cannot load properties file")
    return None

class Config():
    
    def __init__(self, as_json):
        self.as_json = as_json            

    def get_users(self):
        if USERS_SECTION in self.as_json:
            users = []
            for user in self.as_json[USERS_SECTION]:
                name = user[USER_NAME]
                images = []
                for img in user[USER_IMAGES]:
                    images.append(img)
                users.append(AuthorizedUser(name, images))
            return users
        return None
    
    def get_motion_config(self):
        if MOTION_SENSOR_SECTION in self.as_json:
            return MotionConfig(self.as_json[MOTION_SENSOR_SECTION])
        return None

    def get_android_connector_config(self):
        if ANDROID_CONNECTOR_SECTION in self.as_json:
            return AndroidConnectorConfig(self.as_json[ANDROID_CONNECTOR_SECTION])
        return None

    def get_image_folder_location(self):
        if IMAGE_FOLDER in self.as_json:
            return self.as_json[IMAGE_FOLDER]
        return None

class MotionConfig():
    def __init__(self, json):
        self.tries = json[TRIES]
        self.interval = json[INTERVAL]
        self.treshold_weight = json[TRESHOLD_WEIGHT]
        self.drift_weight = json[DRIFT_WEIGHT]
        self.move_min = json[MOVE_MIN]
        self.move_max = json[MOVE_MAX]

class AndroidConnectorConfig():
    def __init__(self, json):
        self.ip_cam_addr = json[IP_CAM_ADDRESS]
        self.max_measurements = json[MAX_MEASUREMENTS]
        self.sensor_data_endpoint = json[SENSOR_DATA_ENDPOINT]
        self.photo_endpoint = json[PHOTO_ENDPOINT]
        self.tmp_folder_location = json[TMP_FOLDER]
        self.last_photo_file_name = json[TMP_FILE_NAME]