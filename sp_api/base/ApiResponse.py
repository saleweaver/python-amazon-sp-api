import pprint


class ApiResponse:
    def __init__(self, payload=None, errors=None, pagination=None, headers=None, nextToken=None, **kwargs):
        self.payload = payload or kwargs
        self.errors = errors
        self.pagination = pagination
        self.headers = headers
        self.rate_limit = self.set_rate_limit(headers)
        self.next_token = self.set_next_token(nextToken)
        if kwargs != self.payload:
            self.kwargs = kwargs

    def __str__(self):
        return pprint.pformat(self.__dict__)

    def set_next_token(self, nextToken=None):
        if nextToken:
            return nextToken
        try:
            return self.payload.get('NextToken', None)
        except AttributeError:
            return None

    @staticmethod
    def set_rate_limit(headers: dict = None):
        try:
            return headers['x-amzn-RateLimit-Limit']
        except (AttributeError, KeyError, TypeError):
            return None
