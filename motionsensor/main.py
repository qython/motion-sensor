from motionsensor.motion_sensor import MotionSensor
from motionsensor.config import load_config
from motionsensor.android_connector import AndroidConnector
from motionsensor.face_recognition import FaceRecognition

import sys
import os

config = load_config("properties.json")

if config is None:
    exit

face_recognition_config = config.get_face_recognition_config()
motion_config = config.get_motion_config()
connector_config = config.get_android_connector_config()

if motion_config is None or connector_config is None or face_recognition_config is None:
    print("Kind of problem with configuration file. Cannot start up properly.")
    sys.exit()

connector = AndroidConnector(connector_config)
ms = MotionSensor(motion_config, connector)
    
face_recognition = FaceRecognition(face_recognition_config)

while(True):
    if ms.detect() == True:
        print("Motion detected! Face recognizing...")
        connector.download_photo_to_tmp_folder()
        if face_recognition.compare(connector.path_to_tmp_file):
            print("User recognized! Door is being opened!")
        else:
            print("A stranger has arrived. Door is being kept locked.")
