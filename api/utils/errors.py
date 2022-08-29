class Error(object):

    def __init__(self, msg):

        self.__error = {
            "errors": msg
        }

    @classmethod
    def error(self):

        return self.__error
