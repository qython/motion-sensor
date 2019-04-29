import sys
import os

sys.path.append('../motion-sensor')

from motionsensor.face_recognition import FaceRecognition
from motionsensor.authorized_user import AuthorizedUser

IMAGE_FOLDER_LOCATION = "test/resources/images"

USERS = [
    AuthorizedUser("Bonus", ['bonus.jpg', 'bonus2.jpg']),
    AuthorizedUser("Adrian", [ "adrian.jpg" ])
]

def test_create_face_recognition_class_instance():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    assert faceRecognition != None

def test_compare_the_same_images():
    path_to_image = os.path.join(IMAGE_FOLDER_LOCATION, "adrian.jpg")
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    result = faceRecognition.compare(path_to_image)
    assert result == "Adrian"

def test_compare_similar_images():
    image_name = "bonus3.jpg"
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    result = faceRecognition.compare(os.path.join(IMAGE_FOLDER_LOCATION, image_name))
    assert result == "Bonus"