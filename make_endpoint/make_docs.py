import os
import re

dirs = [
    'listings_items',
    'product_type_definitions',
    'catalog_items'
]


def to_class_name(s):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s[0].upper() + s[1:])


def get_endpoint_link(s):
    return f"""    endpoints/{s}
"""


def get_endpoint_file_template(s):
    class_name = to_class_name(s)
    return f"""{class_name}
{'=' * len(class_name)}
    
    
..  autoclass:: sp_api.api.{class_name}"""


def append_to_links(link):
    with open('../docs/endpoints.rst', 'a') as f:
        f.write(link)
    f.close()


def create_endpoint_file(file_contents, endpoint):
    with open(f'../docs/endpoints/{endpoint}.rst', 'w+') as f:
        f.write(file_contents)
    f.close()


if __name__ == '__main__':
    for endpoint in dirs:
        append_to_links(get_endpoint_link(endpoint))
        create_endpoint_file(get_endpoint_file_template(endpoint), endpoint)
