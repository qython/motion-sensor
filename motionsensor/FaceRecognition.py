import face_recognition
from os import listdir
from os.path import isfile, join

class FaceRecognition(object):

    def __init__(self, users, image_dir_location):
        self.__users = users
        self.__image_dir_location = image_dir_location

    def compare(self, detected_image_location):
        for user in self.__users:
            for f in user.get_file_list():
                file_name = join(self.__image_dir_location, f)
                if(isfile(file_name)):
                    result = self.__is_recognized(file_name, detected_image_location)
                    if(result):
                        return user.get_username()
        return None

    def __is_recognized(self, authorized_image_location, detected_image_location):
        authorized_image = face_recognition.load_image_file(authorized_image_location)
        detected_image = face_recognition.load_image_file(detected_image_location)

        authorized_encoding = face_recognition.face_encodings(authorized_image)[0]
        detected_encoding = face_recognition.face_encodings(detected_image)[0]

        return face_recognition.compare_faces([authorized_encoding], detected_encoding)