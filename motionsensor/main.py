from motionsensor.motion_sensor import MotionSensor
from motionsensor.config import load_config
from android_connector import AndroidConnector

config = load_config("properties.json")

if config is None:
    exit

users = config.get_users()
img_dir = config.get_image_folder_location()

motion_config = config.get_motion_config()
connector_config = config.get_android_connector_config()

if motion_config is not None and connector_config is not None:

    connector = AndroidConnector(connector_config)
    ms = MotionSensor(connector, motion_config.tries, motion_config.interval, motion_config.treshold_weight, motion_config.drift_weight, motion_config.move_min, motion_config.move_max)
    while(True):
        if ms.detect() == True:
            print("Motion detected: 1")
        else:
            print("Motion detected: 0")
