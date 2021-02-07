import pprint


class ApiResponse:
    def __init__(self, payload=None, errors=None, pagination=None, headers=None):
        self.payload = payload
        self.errors = errors
        self.pagination = pagination
        self.headers = headers

    def __str__(self):
        return pprint.pformat(self.__dict__)

