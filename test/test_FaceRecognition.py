import sys
import os
sys.path.append('../motion-sensor')

from motionsensor.FaceRecognition import FaceRecognition
from motionsensor.AuthorizedUser import AuthorizedUser

IMAGE_FOLDER_LOCATION = "test/resources/images"
IMAGE_NAME = "image.jpg"

USERS = [
    AuthorizedUser("Adrian", [ "image.jpg" ])
]

def test_createFaceRecognitionInstance():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    assert faceRecognition != None

def test_compareImages():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    result = faceRecognition.compare(os.path.join(IMAGE_FOLDER_LOCATION, IMAGE_NAME))
    assert result == "Adrian"