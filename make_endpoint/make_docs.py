import os
import re

dirs = [
    'listings_restrictions'
]


def to_class_name(s):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s[0].upper() + s[1:])


def get_endpoint_link(s):
    return """    endpoints/{}
""".format(s)


def get_endpoint_file_template(s):
    class_name = to_class_name(s)
    return """{}
{}
    
    
..  autoclass:: sp_api.api.{}""".format(class_name, '=' * len(class_name), class_name)


def append_to_links(link):
    with open('../docs/endpoints.rst', 'a') as f:
        f.write(link)
    f.close()


def create_endpoint_file(file_contents, endpoint):
    with open('../docs/endpoints/{}.rst'.format(endpoint), 'w+') as f:
        f.write(file_contents)
    f.close()


if __name__ == '__main__':
    for endpoint in dirs:
        append_to_links(get_endpoint_link(endpoint))
        create_endpoint_file(get_endpoint_file_template(endpoint), endpoint)
