class AuthorizedUser(object):

    def __init(self, username, file_list):
        self.__username = username
        self.__file_list = file_list

    def get_username(self):
        return self.__username
    
    def get_file_list(self):
        return self.__file_list