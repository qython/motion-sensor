import json
from os.path import isfile
from motionsensor.authorized_user import AuthorizedUser

USERS_SECTION = "users"
USER_NAME = "name"
USER_IMAGES = "images"

IMAGE_FOLDER = "image_folder_location"

class Config():
    
    def __init__(self, file_name):
        properties = self.__load_config(file_name)

        if properties is not None:
            self.__authenticated_users = self.__load_users(properties)
            self.__image_folder_location = self.__load_image_folder_location(properties)
    
    def __load_config(self, file):
        if not isfile(file):
            return None
        try:
            f = open(file, 'r')
            loaded = json.loads(f.read())
            f.close()
            return loaded
        except IOError:
            print("ERROR: Cannot load properties file")
        return None

    def __load_users(self, props):
        if USERS_SECTION in props:
            users = []
            for user in props[USERS_SECTION]:
                name = user[USER_NAME]
                images = []
                for img in user[USER_IMAGES]:
                    images.append(img)
                users.append(AuthorizedUser(name, images))
            return users
        return None
    
    def __load_image_folder_location(self, props):
        if IMAGE_FOLDER in props:
            return props[IMAGE_FOLDER]
        return None

    def get_users(self):
        return self.__authenticated_users
    
    def get_image_folder_location(self):
        return self.__image_folder_location