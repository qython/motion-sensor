import sys
sys.path.append('/mnt/data/Workspace/motion-sensor')

from motionsensor.FaceRecognition import FaceRecognition
from motionsensor.AuthorizedUser import AuthorizedUser

IMAGE_FOLDER_LOCATION = "resources/test_images"
IMAGE_NAME = "image.png"

USERS = [
    AuthorizedUser("Doge", [ "image.png" ])
]

def createFaceRecognitionInstance():
    faceRecognition = FaceRecognition(USERS, IMAGE_FOLDER_LOCATION)
    assert faceRecognition != None