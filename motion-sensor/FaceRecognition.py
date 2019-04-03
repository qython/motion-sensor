import face_recognition
from os import listdir
from os.path import isfile, join

class FaceRecognition(object):

    AUTHORISED_USERS_FOLDER = "../authorised"

    def __init__(self):
        reload_authorised_users()

    def reload_authorised_users(self):
        self.authorized_names = [f for f in listdir(self.AUTHORISED_USERS_FOLDER) if isfile(join(self.AUTHORISED_USERS_FOLDER, f))]
        
    def compare(self, detected_image_path):
        for (f in self.authorized_names):
            if(isfile(f)):
                authorized_image = face_recognition.load_image_file(f)
                detected_image = face_recognition.load_image_file(detected_image_path)

                authorized_encoding = face_recognition.face_encodings(authorized_image)[0]
                detected_encoding = face_recognition.face_encodings(detected_image)[0]

                if(face_recognition.compare_faces([authorized_encoding], detected_encoding)):
                    return True
        return False

