from motionsensor.motion_sensor import MotionSensor
from motionsensor.config import load_config
from motionsensor.android_connector import AndroidConnector
from motionsensor.face_rec import FaceRecognition

import sys
import os
import logging
logger = logging.getLogger(__name__)

config = load_config("properties.json")

if config is None:
    logger.error("Cannot open config file")
    exit

face_recognition_config = config.get_face_recognition_config()
motion_config = config.get_motion_config()
connector_config = config.get_android_connector_config()

if motion_config is None or connector_config is None or face_recognition_config is None:
    logger.error("Kind of problem with configuration file. Cannot start up properly.")
    sys.exit()

connector = AndroidConnector(connector_config)
ms = MotionSensor(motion_config, connector)
face_recognition = FaceRecognition(face_recognition_config)

logger.info("===== MOTION SENSOR STARTED =====")

while(True):
    if ms.detect() == True:
        logger.info("Motion detected! Trying to recognize face.")
        connector.download_photo_to_tmp_folder()
        if face_recognition.compare(connector.path_to_tmp_file):
            logger.info("User recognized! Door is being opened!")
        else:
            logger.warning("A stranger has arrived. Door is being kept locked.")
