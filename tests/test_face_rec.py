import os

from motionsensor.face_rec import FaceRecognition
from motionsensor.authorized_user import AuthorizedUser
from motionsensor.config import load_config

PROPS_FILE = os.path.join(os.path.dirname(__file__), os.path.normpath("resources/props.json"))

config = load_config(PROPS_FILE)
face_recognition_config = config.get_face_recognition_config()

TEST_USER_1_NAME = "Adrian"
TEST_USER_1_IMAGE = "adrian.jpg"
TEST_USER_2_NAME = "Bonus"
TEST_USER_2_IMAGE = "bonus3.jpg"
EXPECTED_IMAGE_FOLDER_LOCATION = os.path.normpath("tests/resources/images")

def test_create_face_recognition_class_instance():
    faceRecognition = FaceRecognition(face_recognition_config)
    assert faceRecognition != None

def test_compare_the_same_images():
    face_recognition = FaceRecognition(face_recognition_config)
    result = face_recognition.compare(os.path.join(face_recognition_config.image_folder_location, TEST_USER_1_IMAGE))
    assert result == TEST_USER_1_NAME

def test_compare_similar_images():
    face_recognition = FaceRecognition(face_recognition_config)
    result = face_recognition.compare(os.path.join(face_recognition_config.image_folder_location, TEST_USER_2_IMAGE))
    assert result == TEST_USER_2_NAME