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
        return wrapper
    return decorator


def encrypt_aes(file_or_bytes_io, key, iv):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(pad(bytes(file_or_bytes_io.read(), encoding='iso-8859-1'), 16))


def decrypt_aes(content, key, iv):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    decrypter = AES.new(key, AES.MODE_CBC, iv)
    return decrypter.decrypt(content)

