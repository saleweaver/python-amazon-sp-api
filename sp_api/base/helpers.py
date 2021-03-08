from Crypto.Util.Padding import pad

import base64
from Crypto.Cipher import AES

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
        wrapper.__doc__ = function.__doc__
        return wrapper
    return decorator


def encrypt_aes(file_or_bytes_io, key, iv):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    aes = AES.new(key, AES.MODE_CBC, iv)
    try:
        return aes.encrypt(pad(bytes(file_or_bytes_io.read(), encoding='iso-8859-1'), 16))
    except UnicodeEncodeError:
        return aes.encrypt(pad(bytes(file_or_bytes_io.read(), encoding='utf-8'), 16))
    except TypeError:
        return aes.encrypt(pad(file_or_bytes_io.read(), 16))


def decrypt_aes(content, key, iv):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    decrypter = AES.new(key, AES.MODE_CBC, iv)
    return decrypter.decrypt(content)


def nest_dict(flat: dict()):
    """
    Convert flat dictionary to nested dictionary.

    Input
    {
        "AmazonOrderId":1,
        "ShipFromAddress.Name" : "Seller",
        "ShipFromAddress.AddressLine1": "Street",
    }

    Output
    {
        "AmazonOrderId":1,
        "ShipFromAddress.: {
            "Name" : "Seller",
            "AddressLine1": "Street",
        }
    }


    Args:
        flat:dict():

    Returns:
        nested:dict():
    """

    result = {}
    for k, v in flat.items():
        _nest_dict_rec(k, v, result)
    return result


def _nest_dict_rec(k, v, out):
    k, *rest = k.split('.', 1)
    if rest:
        _nest_dict_rec(rest[0], v, out.setdefault(k, {}))
    else:
        out[k] = v

