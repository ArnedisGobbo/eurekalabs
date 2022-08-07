class APIException(BaseException):
    def __init__(self):
        self.msg = ""
        super(APIException, self).__init__(self)

    def __str__(self):
        return self.msg


class InputErrorException(APIException):
    def __init__(self, msg):
        super(InputErrorException, self).__init__()
        self.msg = msg


class InvalidLogPath(InputErrorException):
    def __init__(self, log_path):
        msg = ("The log directory '{}' doesn't exist, or you don't have "
               "permission over it").format(log_path)
        self.msg = msg
