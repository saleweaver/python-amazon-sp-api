import pprint


class ApiResponse:
    def __init__(self, payload=None, errors=None, pagination=None, headers=None, nextToken=None, **kwargs):
        self.payload = payload
        self.errors = errors
        self.pagination = pagination
        self.headers = headers
        self.next_token = nextToken
        self.kwargs = kwargs

    def __str__(self):
        return pprint.pformat(self.__dict__)

