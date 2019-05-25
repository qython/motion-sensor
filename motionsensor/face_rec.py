import face_recognition
from os import listdir
from os.path import isfile, join

import logging
logger = logging.getLogger(__name__)

class FaceRecognition(object):

    def __init__(self, config):
        self.__users = config.users
        self.__image_dir_location = config.image_folder_location

    def compare(self, detected_image_location):
        logger.debug("Comparing...")
        for user in self.__users:
            logger.debug("----- with user: %s" % user.get_username())
            for f in user.get_files_list():
                file_name = join(self.__image_dir_location, f)
                logger.debug("---------- with photo: %s" % file_name)
                if(isfile(file_name)):
                    result = self.__is_recognized(file_name, detected_image_location)
                    if result == True:
                        logger.debug("Face recognized!")
                        return user.get_username()
                    logger.debug("Not known face")
        return None

    def __is_recognized(self, authorized_image_location, detected_image_location):
        logger.debug("Recognizing...")
        authorized_image = face_recognition.load_image_file(authorized_image_location)
        detected_image = face_recognition.load_image_file(detected_image_location)

        authorized_encodings = face_recognition.face_encodings(authorized_image)
        detected_encodings = face_recognition.face_encodings(detected_image)

        logger.debug("Encodings at known photo: %d, encodings at not-known photo: %d" % (len(authorized_encodings), len(detected_encodings)))

        for detected_encoding in detected_encodings:
            results = face_recognition.compare_faces(authorized_encodings, detected_encoding)
            for result in results:
                if result == True:
                    return True
        return False