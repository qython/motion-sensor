import face_recognition
from os import listdir
from os.path import isfile, join

class FaceRecognition(object):

    def __init__(self, config):
        self.__users = config.users
        self.__image_dir_location = config.image_folder_location

    def compare(self, detected_image_location):
        print("Comparing...")
        for user in self.__users:
            print("----- with user: %s" % user.get_username())
            for f in user.get_files_list():
                file_name = join(self.__image_dir_location, f)
                print("---------- with photo: %s" % file_name)
                if(isfile(file_name)):
                    result = self.__is_recognized(file_name, detected_image_location)
                    if result == True:
                        print("Face recognized!")
                        return user.get_username()
                    print("Not known face")
        return None

    def __is_recognized(self, authorized_image_location, detected_image_location):
        print("Recognizing...")
        authorized_image = face_recognition.load_image_file(authorized_image_location)
        detected_image = face_recognition.load_image_file(detected_image_location)

        authorized_encodings = face_recognition.face_encodings(authorized_image)
        detected_encodings = face_recognition.face_encodings(detected_image)

        print("Encodings at known photo: %d, encodings at not-known photo: %d" % (len(authorized_encodings), len(detected_encodings)))

        for detected_encoding in detected_encodings:
            results = face_recognition.compare_faces(authorized_encodings, detected_encoding)
            for result in results:
                if result == True:
                    return True
        return False