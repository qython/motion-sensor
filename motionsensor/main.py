from motionsensor.motion_sensor import MotionSensor
from motionsensor.config import load_config
from motionsensor.android_connector import AndroidConnector
from motionsensor.face_rec import FaceRecognition
import urllib
import time

import sys
import os

config = load_config("properties.json")

if config is None:
    print("Cannot open config file")
    sys.exit()

face_recognition_config = config.get_face_recognition_config()
motion_config = config.get_motion_config()
connector_config = config.get_android_connector_config()

if motion_config is None or connector_config is None or face_recognition_config is None:
    print("Kind of problem with configuration file. Cannot start up properly.")
    sys.exit()

connector = AndroidConnector(connector_config)
ms = MotionSensor(motion_config, connector)
face_recognition = FaceRecognition(face_recognition_config)

print("========== MOTION SENSOR STARTED ===========")
print("=== Server IP: %s ===" % connector.url)
print("============================================")

try:
    while(True):
        if ms.detect() == True:
            print("Motion detected!")
            print("Downloading actual photo.")
            connector.download_photo_to_tmp_folder()
            comparision_result = face_recognition.compare(connector.path_to_tmp_file)
            if comparision_result is not None:
                print("========================================")
                print("User recognized! It is %s! Door is being opened!" % comparision_result)
                time.sleep(3)
                print("========================================"
            else:
                print("Face not recognized.")
except KeyboardInterrupt as e:
    print("Program stopped.")
except urllib.error.URLError as e:
    print("Connection with server could not get established or has been lost. Program is being ended.")