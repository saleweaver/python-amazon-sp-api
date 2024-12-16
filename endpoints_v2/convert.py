import json
import re
import sys
from pathlib import Path

def load_swagger(swagger_file):
    with open(swagger_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_version(info):
    # Extract version from the info block
    return info.get("version", "v1")

def normalize_path(path_str, version):
    # Replace the actual version in the path with <version>
    pattern = r'/'+re.escape(version)+r'(\b|/)'
    return re.sub(pattern, '<version>/', path_str)

def to_snake_case(name):
    # Convert a string (likely camelCase or PascalCase) to snake_case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()

def generate_method_name(path_str, method):
    segments = [seg for seg in path_str.split('/') if seg and not seg.startswith('<')]
    if not segments:
        base_name = 'root'
    else:
        base_name = segments[-1]
    if method.lower() == 'get':
        fname = f'get_{base_name}'
    elif method.lower() == 'post':
        fname = f'submit_{base_name}'
    elif method.lower() == 'put':
        fname = f'update_{base_name}'
    elif method.lower() == 'delete':
        fname = f'delete_{base_name}'
    else:
        fname = f'{method.lower()}_{base_name}'
    return fname.lower().replace('-', '_')

def generate_code(swagger_data):
    info = swagger_data.get("info", {})
    paths = swagger_data.get("paths", {})

    version = extract_version(info)

    class_name_base = "VendorShipments"
    version_enum_class = "VendorShipmentsVersion"
    factory_class = class_name_base
    versioned_class = f"{class_name_base}V{version.replace('v','')}"

    endpoints = []
    for path, path_obj in paths.items():
        for method, method_obj in path_obj.items():
            summary = method_obj.get("summary", "")
            operation_id = method_obj.get("operationId")

            # Determine method name
            if operation_id:
                fname = to_snake_case(operation_id)
            else:
                normalized_path = normalize_path(path, version)
                fname = generate_method_name(normalized_path, method)

            # Check if we have a body parameter (for POST/PUT)
            if method.lower() == 'get':
                # GET requests typically use params
                endpoint_code = f"""    @sp_endpoint("{normalize_path(path, version)}", method="{method.upper()}")
    def {fname}(self, **kwargs) -> ApiResponse:
        \"\"\"{summary}\"\"\"
        return self._request(kwargs.pop("path"), params=kwargs)
"""
            else:
                # For non-GET methods, check parameters
                has_body = any(p.get("in") == "body" for p in method_obj.get("parameters", []))
                if has_body:
                    endpoint_code = f"""    @sp_endpoint("{normalize_path(path, version)}", method="{method.upper()}")
    def {fname}(self, data, **kwargs) -> ApiResponse:
        \"\"\"{summary}\"\"\"
        return self._request(kwargs.pop("path"), data={{**data, **kwargs}})
"""
                else:
                    endpoint_code = f"""    @sp_endpoint("{normalize_path(path, version)}", method="{method.upper()}")
    def {fname}(self, **kwargs) -> ApiResponse:
        \"\"\"{summary}\"\"\"
        return self._request(kwargs.pop("path"), params=kwargs)
"""

            endpoints.append(endpoint_code)

    endpoints_str = "\n".join(endpoints)

    code_template = f'''import enum
import os
from sp_api.base import Client, Marketplaces, ApiResponse, sp_endpoint, fill_query_params

class {version_enum_class}(str, enum.Enum):
    V_1 = "{version}"
    LATEST = "{version}"

class {factory_class}(Client):
    """
    Vendor Shipments SP-API Client Factory
    """
    _version_mapping = {{
        "{version}": None  # will be set after class definition
    }}

    def __new__(cls, *args, **kwargs):
        version = kwargs.pop("version", {version_enum_class}.LATEST)
        if isinstance(version, {version_enum_class}):
            version = version.value
        elif not isinstance(version, str):
            raise ValueError("Version must be a string or {version_enum_class} Enum member.")

        selected_class = cls._version_mapping.get(version)
        if not selected_class:
            raise ValueError(f"Unsupported version: {{version}}")

        instance = super({factory_class}, cls).__new__(selected_class)
        return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class {versioned_class}({factory_class}):
    version: {version_enum_class} = {version_enum_class}.V_1

{endpoints_str}

{factory_class}._version_mapping["{version}"] = {versioned_class}
'''
    return code_template


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_code.py <swagger.json> <output.py>")
        sys.exit(1)

    swagger_file = sys.argv[1]
    output_file = sys.argv[2]

    swagger_data = load_swagger(swagger_file)
    code = generate_code(swagger_data)

    Path(output_file).write_text(code, encoding='utf-8')
    print(f"Generated code in {output_file}")