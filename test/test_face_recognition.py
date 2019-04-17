import sys
import os
sys.path.append('../motion-sensor')

from motionsensor.face_recognition import FaceRecognition
from motionsensor.authorized_user import AuthorizedUser

IMAGE_FOLDER_LOCATION = "test/resources/images"
IMAGE_NAME = "image.jpg"

USERS = [
    AuthorizedUser("Adrian", [ "image.jpg" ])
]

def test_create_face_recognition_class_instance():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    assert faceRecognition != None

def test_compare_images():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    result = faceRecognition.compare(os.path.join(IMAGE_FOLDER_LOCATION, IMAGE_NAME))
    assert result == "Adrian"