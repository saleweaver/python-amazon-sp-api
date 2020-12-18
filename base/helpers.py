def fill_query_params(query, *args):
    return query.format(*args)


def sp_endpoint(path, method='GET'):
    def decorator(function):
        def wrapper(*args, **kwargs):
            kwargs.update({
                'path': path,
                'method': method
            })
            return function(*args, **kwargs)
        return wrapper
    return decorator
