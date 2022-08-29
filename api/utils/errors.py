class Error(object):

    def __set_error(self, msg):

        self.__error = {
            "errors": msg
        }

    @classmethod
    def error(cls, msg):
        Error.__set_error(cls, msg)

        return Error.__error
