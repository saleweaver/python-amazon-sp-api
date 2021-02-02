class SellingApiException(BaseException):
    """
    Generic Exception

    Parameters:

        message: str The error message
        amzn_code: str Amazon Error Code
        error: list Amazon Error list

    """
    code = 999

    def __init__(self, error):
        try:
            self.message = error[0].get('message')
            self.amzn_code = error[0].get('code')
        except IndexError:
            pass
        self.error = error


class SellingApiBadRequestException(SellingApiException):
    """
    400	Request has missing or invalid parameters and cannot be parsed.
    """
    code = 400

    def __init__(self, error):
        super(SellingApiBadRequestException, self).__init__(error)


class SellingApiForbiddenException(SellingApiException):
    """
    403	Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """
    code = 403

    def __init__(self, error):
        super(SellingApiForbiddenException, self).__init__(error)


class SellingApiNotFoundException(SellingApiException):
    """
    404	The resource specified does not exist.
    """
    code = 404

    def __init__(self, error):
        super(SellingApiNotFoundException, self).__init__(error)


class SellingApiRequestThrottledException(SellingApiException):
    """
    429	The frequency of requests was greater than allowed.
    """
    code = 429

    def __init__(self, error):
        super(SellingApiRequestThrottledException, self).__init__(error)


class SellingApiServerException(SellingApiException):
    """
    500	An unexpected condition occurred that prevented the server from fulfilling the request.
    """
    code = 500

    def __init__(self, error):
        super(SellingApiServerException, self).__init__(error)


class SellingApiTemporarilyUnavailableException(SellingApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """
    code = 503

    def __init__(self, error):
        super(SellingApiTemporarilyUnavailableException, self).__init__(error)


def get_exception_for_code(code: int):
    return {
        400: SellingApiBadRequestException,
        403: SellingApiForbiddenException,
        429: SellingApiRequestThrottledException,
        500: SellingApiServerException,
        503: SellingApiTemporarilyUnavailableException
    }.get(code, SellingApiException)
