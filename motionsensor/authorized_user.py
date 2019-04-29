class AuthorizedUser(object):

    def __init__(self, username, files_list):
        self.__username = username
        self.__files_list = files_list

    def get_username(self):
        return self.__username
    
    def get_files_list(self):
        return self.__files_list