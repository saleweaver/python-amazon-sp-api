"""
Parser module for Swagger/OpenAPI specification.

This module provides functionality to parse both Swagger 2.0 and OpenAPI 3.x specifications.
It extracts models, enums, request/response relationships, and endpoints to enable
code generation of Pydantic models.
"""

# Standard library imports for file operations, regular expressions, error handling
import os
import re
import json
import yaml
import httpx  # HTTP client for fetching remote specs
import traceback
import sys
from typing import Any, Dict, List, Optional, Set, Tuple, Union  # Type hints
from urllib.parse import urlparse  # For URL validation and parsing

from tabulate import tabulate


class SwaggerParser:
    """
    Parser for Swagger/OpenAPI specifications (both 2.0 and 3.x).

    This class is responsible for parsing Swagger/OpenAPI specifications and extracting
    model definitions, enum values, request/response relationships, and API endpoints.
    It supports both Swagger 2.0 and OpenAPI 3.x formats with appropriate handling
    for the differences between them.
    """

    def __init__(self):
        """
        Initialize the parser with empty collections to store parsed data.

        Creates empty containers for various elements that will be extracted during parsing:
        - models: Dictionary of parsed models keyed by model name
        - enums: Dictionary of parsed enums keyed by enum name
        - request_models: Set of model names used in request bodies
        - responses: Dictionary mapping operation IDs to response models
        - endpoints: List of parsed API endpoints
        - request_params: Dictionary mapping operation IDs to request parameter model names
        """
        self.models = {}  # Stores all model definitions with their properties
        self.enums = {}  # Stores all enum definitions with their values
        self.request_models = set()  # Tracks which models are used in request bodies
        self.responses = {}  # Maps operation IDs to their response models
        self.endpoints = []  # Stores all API endpoint information
        self.request_params = {}  # Maps operation IDs to request parameter model names
        self.client_description = ""
        self.client_version = ""
        self.client_title = ""

    def parse_from_file(self, file_path: str) -> Dict[str, Any]:
        """
        Parse a Swagger/OpenAPI specification from a file.

        This is the main entry point for parsing from a local file. It:
        1. Verifies the file exists
        2. Loads and parses JSON or YAML content based on file extension
        3. Delegates to _parse_swagger for actual parsing

        Args:
            file_path: Path to the Swagger/OpenAPI specification file.

        Returns:
            Dictionary containing all parsed data (models, enums, endpoints, etc.)

        Raises:
            FileNotFoundError: If the specified file doesn't exist
            ValueError: If the file format is not supported
        """
        try:
            # First check if the file exists to provide a clear error
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            # Load swagger spec from file based on its extension
            with open(file_path, "r") as f:
                if file_path.endswith(".json"):
                    # Parse JSON file
                    swagger_spec = json.load(f)
                elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
                    # Parse YAML file
                    swagger_spec = yaml.safe_load(f)
                else:
                    # Reject unsupported file formats
                    raise ValueError(
                        "Unsupported file format. Only JSON and YAML are supported."
                    )

            # Delegate to the internal parsing method
            return self._parse_swagger(swagger_spec)
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception("Error parsing Swagger spec from file", e)
            raise

    def parse_from_url(self, url: str) -> Dict[str, Any]:
        """
        Parse Swagger/OpenAPI specification from a URL.

        This method:
        1. Makes an HTTP request to the specified URL
        2. Determines the content type (JSON or YAML)
        3. Parses the content accordingly
        4. Delegates to _parse_swagger for actual parsing

        Args:
            url: URL to the Swagger/OpenAPI specification.

        Returns:
            Dictionary with parsed models, endpoints, and request/response relationships.

        Raises:
            HTTPError: If the HTTP request fails
            ValueError: If the content cannot be parsed as JSON or YAML
        """
        try:
            # Make HTTP request to get the swagger spec
            response = httpx.get(url)  # Use httpx for HTTP requests
            response.raise_for_status()  # Raise exception for non-200 responses
            response_text = response.text
            response_text = re.sub(
                r'(Request)(?=["\'\s,\}\]]|$)', "RequestBody", response_text
            )
            # Check content type header to determine format
            content_type = response.headers.get("content-type", "")

            # Parse the response based on content type
            if "application/json" in content_type:
                # Content is explicitly JSON
                swagger_spec = json.loads(response_text)
            elif (
                "application/yaml" in content_type
                or "application/x-yaml" in content_type
            ):
                # Content is explicitly YAML
                swagger_spec = yaml.safe_load(response_text)
            else:
                # Try to infer format from content if content-type header is not helpful
                try:
                    # First try JSON
                    swagger_spec = json.loads(response_text)
                except:
                    try:
                        # Then try YAML
                        swagger_spec = yaml.safe_load(response_text)
                    except:
                        raise ValueError(
                            "Could not determine format of Swagger spec from URL."
                        )

            # Delegate to the internal parsing method
            return self._parse_swagger(swagger_spec)
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error parsing Swagger spec from URL: {url}", e)
            raise

    def parse(self, swagger_source: str) -> Dict[str, Any]:
        """
        Parse Swagger/OpenAPI specification from a file or URL.

        This method:
        1. Checks if the source is a URL or a file path
        2. Calls either parse_from_file or parse_from_url accordingly

        Args:
            swagger_source: Path to file or URL containing the specification.

        Returns:
            Dictionary with parsed models, endpoints, and request/response relationships.
        """
        try:
            # Check if the source is a URL
            parsed_url = urlparse(swagger_source)
            if parsed_url.scheme and parsed_url.netloc:
                return self.parse_from_url(swagger_source)
            else:
                return self.parse_from_file(swagger_source)
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error parsing from source: {swagger_source}", e)
            raise

    def _parse_swagger(self, swagger_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse the Swagger/OpenAPI specification.

        This method detects the version of the specification (Swagger 2.0 or OpenAPI 3.x)
        and delegates to the appropriate parsing method. It also resets the parser state
        before starting.

        Args:
            swagger_spec: Swagger/OpenAPI specification as a dictionary.

        Returns:
            Dictionary containing all parsed data (models, enums, endpoints, etc.)
        """
        try:
            # Reset parser state
            self.models = {}
            self.enums = {}
            self.request_models = set()
            self.responses = {}
            self.endpoints = []
            self.request_params = {}  # Reset request parameters
            self.client_description = ""
            self.client_version = ""
            self.client_title = ""

            # Detect OpenAPI version
            if "swagger" in swagger_spec:
                version = swagger_spec["swagger"]
                if version.startswith("2"):
                    self._parse_swagger2(swagger_spec)
                else:
                    raise ValueError(f"Unsupported Swagger version: {version}")
            else:
                raise ValueError("Could not determine Swagger/OpenAPI version.")

            return {
                "models": self.models,
                "enums": self.enums,
                "request_models": self.request_models,
                "responses": self.responses,
                "endpoints": self.endpoints,
                "request_params": self.request_params,  # Include request parameter models,
                "client_description": re.sub('"', "'", re.sub(r'(\n\s*){2,}', '\n    ', self._wrap_text(
                        re.sub(r"\n", "\n    ", self.client_description), 90, 4
                    ).rstrip())),
                "client_version": self.client_version,
                "client_title": self.client_title,
            }
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception("Error parsing Swagger specification", e)
            raise

    def _parse_swagger2(self, swagger_spec: Dict[str, Any]) -> None:
        """
        Parse Swagger 2.0 specification.

        Args:
            swagger_spec: Dictionary containing the Swagger 2.0 specification.
        """
        try:
            # Parse definitions
            definitions = swagger_spec.get("definitions", {})
            for name, schema in definitions.items():
                self._parse_model(name, schema)
            self.client_description = swagger_spec.get("info", {}).get(
                "description", ""
            )
            self.client_version = swagger_spec.get("info", {}).get("version", "")
            self.client_title = swagger_spec.get("info", {}).get("title", "")
            # Parse paths
            paths = swagger_spec.get("paths", {})
            for path, path_item in paths.items():
                for method, operation in path_item.items():
                    if method in ["get", "post", "put", "delete", "patch"]:
                        self._parse_operation_swagger2(path, method, operation)
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception("Error parsing Swagger 2.0 specification", e)
            raise

    def _parse_model(self, name: str, schema: Dict[str, Any]) -> None:
        """
        Parse a model schema.

        Args:
            name: Name of the model.
            schema: Schema definition.
        """
        try:
            # Check if schema is a reference
            if "$ref" in schema:
                ref = schema["$ref"]
                model_name = self._get_ref_name(ref)
                self.models[name] = self.models.get(model_name, {})
                return

            # Check if schema is an array type
            if schema.get("type") == "array" and "items" in schema:
                items_schema = schema.get("items", {})
                if "$ref" in items_schema:
                    ref_name = self._get_ref_name(items_schema["$ref"])
                    self.models[name] = {
                        "name": name,
                        "description": re.sub('"', "'", re.sub(
                            r"\s+|\n",
                            " ",
                            re.sub(r"\s+|\n+", " ", schema.get("description", "")),
                        )),
                        "is_array": True,
                        "item_type": "model",
                        "model_name": ref_name,
                        "pydantic_type": f"List[{ref_name}]",
                        "properties": {},  # Add empty properties to maintain structure compatibility
                    }
                    return

            # Check if schema is a primitive type with no properties
            primitive_types = {
                "string": "str",
                "integer": "int",
                "number": "float",
                "boolean": "bool",
            }
            schema_type = schema.get("type")

            if schema_type in primitive_types and not schema.get("properties"):
                # This is a primitive type without properties - treat as a type alias
                self.models[name] = {
                    "name": name,
                    "description": re.sub('"', "'", re.sub(
                        r"\s+|\n",
                        " ",
                        re.sub(r"\s+|\n+", " ", schema.get("description", "")),
                    )),
                    "is_primitive": True,
                    "primitive_type": primitive_types[schema_type],
                    "pydantic_type": primitive_types[schema_type],
                    "properties": {},  # Add empty properties to maintain structure compatibility
                }
                return

            # Get properties
            properties = {}
            required_props = schema.get("required", [])

            for prop_name, prop_schema in schema.get("properties", {}).items():
                snake_prop_name = self.to_snake_case(prop_name)
                properties[snake_prop_name] = self._parse_property(
                    prop_name, prop_schema, prop_name in required_props, model_context=name
                )
                # Keep original name for reference
                properties[snake_prop_name]["name"] = prop_name

            # Store the model
            self.models[name] = {
                "name": name,
                "description": re.sub('"', "'", re.sub(
                        r"\s+|\n",
                        " ",
                        re.sub(r"\s+|\n+", " ", schema.get("description", "")),
                    )),
                "properties": properties,
            }
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error parsing model: {name}", e)
            raise

    def _parse_property(
        self, original_name: str, schema: Dict[str, Any], required: bool, model_context: str = ""
    ) -> Dict[str, Any]:
        """
        Parse a property schema.

        Args:
            original_name: Original name of the property.
            schema: Schema definition.
            required: Whether the property is required.

        Returns:
            Dictionary with parsed property information.
        """
        try:
            # Get property type
            prop_type = self._get_type(schema)

            # Handle reference
            if prop_type == "ref":
                ref_name = self._get_ref_name(schema["$ref"])
                return {
                    "type": "model",
                    "model_name": ref_name,
                    "required": required,
                    "description": re.sub('"', "'", re.sub(
                        r"\s+|\n+", " ", schema.get("description", "")
                    )),
                    "pydantic_type": ref_name,
                }

            # Handle array
            if prop_type == "array":
                items_schema = schema.get("items", {})
                items_type = self._get_type(items_schema)

                # Handle array of references
                if items_type == "ref":
                    ref_name = self._get_ref_name(items_schema["$ref"])
                    return {
                        "type": "array",
                        "item_type": "model",
                        "model_name": ref_name,
                        "required": required,
                        "description": re.sub('"', "'", re.sub(
                            r"\s+|\n+", " ", schema.get("description", "")
                        )),
                        "pydantic_type": f"List[{ref_name}]",
                    }

                # Handle array of enums - this is where we extract and create enum types from arrays
                elif "enum" in items_schema:
                    # Create a proper enum class name based on the property name
                    # For example, property "status_codes" becomes "StatusCodesEnum"
                    enum_name = self._create_unique_enum_name(original_name, model_context)

                    # Extract enum values from the OpenAPI schema
                    # These are the allowed values for items in the array
                    enum_values = items_schema.get("enum", [])
                    enum_descriptions = None

                    # Look for extended enum documentation in x-docgen-enum-table-extension
                    # This Swagger extension provides descriptions for each enum value
                    if "x-docgen-enum-table-extension" in items_schema:
                        enum_extensions = items_schema["x-docgen-enum-table-extension"]
                        # Create a mapping from enum values to their descriptions
                        enum_descriptions = {
                            ext.get("value"): ext.get("description")
                            for ext in enum_extensions
                            if "value" in ext and "description" in ext
                        }

                    # Store the enum definition in the parser's enum collection
                    # This makes it available for the generator to render later
                    base_type = items_schema.get(
                        "type", "string"
                    )  # Get enum base type (string, integer, etc.)
                    self.enums[enum_name] = {
                        "name": enum_name,  # Enum class name
                        "description": f"Enum for {original_name}",  # Generated description
                        "values": enum_values,  # Allowed values
                        "base_type": base_type,  # Base type (string, integer, etc.)
                        "descriptions": enum_descriptions,  # Value descriptions if available
                    }

                    # Return the property definition with enum type information
                    return {
                        "type": "enum",  # This is an enum property
                        "enum_name": enum_name,  # Name of the enum class
                        "enum_values": enum_values,  # Allowed values
                        "required": required,  # Whether this property is required
                        "description": re.sub('"', "'", re.sub(
                            r"\s+|\n+", " ", schema.get("description", "")
                        )),  # Property description
                        "pydantic_type": f"List[{enum_name}]",  # Resulting Pydantic type annotation
                        "is_array": True,  # Flag indicating this is an array
                        "array_collection_format": schema.get(
                            "collectionFormat", ""
                        ),  # How array items are formatted
                    }

                # Handle array of primitive types (strings, integers, etc.)
                else:
                    # Convert the OpenAPI type to the corresponding Pydantic type
                    item_type = self._get_pydantic_type(items_type)
                    return {
                        "type": "array",  # This is an array property
                        "item_type": items_type,  # Type of items in the array
                        "required": required,  # Whether this property is required
                        "description": re.sub('"', "'", re.sub(
                            r"\s+|\n+", " ", schema.get("description", "")
                        )),  # Property description
                        "pydantic_type": f"List[{item_type}]",  # Resulting Pydantic type annotation
                    }

            # Handle object type properties (Dictionary/JSON objects)
            if prop_type == "object":
                return {
                    "type": "object",  # This is an object property
                    "required": required,  # Whether this property is required
                    "description": re.sub('"', "'", re.sub(
                        r"\s+|\n+", " ", schema.get("description", "")
                    )),  # Property description
                    "pydantic_type": "Dict[str, Any]",  # Resulting Pydantic type annotation
                }

            # Handle enum properties - this is the main enum extraction logic
            if "enum" in schema:
                # Create a proper enum class name based on the property name
                # For example, property "status" becomes "StatusEnum"
                enum_name = self._create_unique_enum_name(original_name, model_context)

                # Extract enum values from the OpenAPI schema
                enum_values = schema.get("enum", [])
                enum_descriptions = None

                # Look for extended enum documentation in x-docgen-enum-table-extension
                # This Swagger extension provides descriptions for each enum value
                if "x-docgen-enum-table-extension" in schema:
                    enum_extensions = schema["x-docgen-enum-table-extension"]
                    # Create a mapping from enum values to their descriptions
                    enum_descriptions = {
                        ext.get("value"): ext.get("description")
                        for ext in enum_extensions
                        if "value" in ext and "description" in ext
                    }

                # Store the enum definition in the parser's enum collection
                # This makes it available for the generator to render later
                base_type = schema.get(
                    "type", "string"
                )  # Get enum base type (string, integer, etc.)
                self.enums[enum_name] = {
                    "name": enum_name,  # Enum class name
                    "description": f"Enum for {original_name}",  # Generated description
                    "values": enum_values,  # Allowed values
                    "base_type": base_type,  # Base type (string, integer, etc.)
                    "descriptions": enum_descriptions,  # Value descriptions if available
                }

                # Return the property definition with enum type information
                return {
                    "type": "enum",  # This is an enum property
                    "enum_name": enum_name,  # Name of the enum class
                    "enum_values": enum_values,  # Allowed values
                    "required": required,  # Whether this property is required
                    "description": re.sub('"', "'", re.sub(
                        r"\s+|\n+", " ", schema.get("description", "")
                        )),  # Property description
                    "pydantic_type": enum_name,  # Resulting Pydantic type annotation
                }

            # Handle basic types (string, integer, number, boolean, etc.)
            pydantic_type = self._get_pydantic_type(prop_type)
            return {
                "type": prop_type,
                "required": required,
                "description": re.sub('"', "'", re.sub(r"\s+|\n+", " ", schema.get("description", ""))),
                "pydantic_type": pydantic_type,
            }
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error parsing property: {original_name}", e)
            raise

    def _create_unique_enum_name(self, property_name: str, model_context: str = "") -> str:
        """
        Create a unique enum name by combining model context and property name.

        Args:
            property_name: Name of the property containing the enum
            model_context: Name of the model this enum belongs to

        Returns:
            Unique enum class name
        """
        # Convert property name to PascalCase
        property_pascal = self.to_pascal_case(property_name)

        if model_context:
            # Convert model context to PascalCase and combine
            model_pascal = self.to_pascal_case(model_context)
            enum_name = f"{model_pascal}{property_pascal}Enum"
        else:
            enum_name = f"{property_pascal}Enum"

        return enum_name


    def _parse_operation_swagger2(
        self, path: str, method: str, operation: Dict[str, Any]
    ) -> None:
        """
        Parse a Swagger 2.0 operation.

        This method extracts information from a Swagger 2.0 API operation, including:
        1. Query and path parameters (used to create request parameter models)
        2. Body parameters (reference to request body schema)
        3. Responses (reference to response schema)

        The extracted information is stored in the parser's internal state for later use
        by the generator.

        Args:
            path: URL path.
            method: HTTP method.
            operation: Operation definition.
        """
        try:
            # Use the operationId from the spec or generate one based on method and path
            # This ID is used to uniquely identify the operation
            operation_id = operation.get("operationId", f"{method}_{path}")
            description = operation.get("description", "")
            # Extract query and path parameters and create a request parameter model
            # This model will contain all query and path parameters as properties
            request_model = None
            if "parameters" in operation:
                # Delegate to _create_request_model to handle parameter extraction
                # This will create a model class for the parameters and return its name
                request_model = self._create_request_model(
                    operation_id, operation.get("parameters", []), path, method
                )

            # Extract request body parameters (Swagger 2.0 style)
            # In Swagger 2.0, body parameters are in the parameters array with "in": "body"
            request_body = None
            for param in operation.get("parameters", []):
                # Look for parameters with "in": "body" which represent request bodies
                if param.get("in") == "body":
                    schema = param.get("schema", {})
                    # If the body references another schema, extract and store that reference
                    if "$ref" in schema:
                        # Get the referenced model name from the $ref path
                        request_body = self._get_ref_name(schema["$ref"])
                        # Mark this model as being used in request bodies
                        # This allows the generator to handle it specially
                        self.request_models.add(request_body)

            # Extract response schemas for different status codes
            # These map HTTP status codes to response model references
            responses = {}
            for status, response in operation.get("responses", {}).items():
                schema = response.get("schema", {})
                # If the response references another schema, extract and store that reference
                if "$ref" in schema:
                    response_model = self._get_ref_name(schema["$ref"])
                    responses[status] = response_model

            # Store endpoint information in the endpoints list
            # This captures the complete API operation data
            self.endpoints.append(
                {
                    "path": path,  # API path
                    "method": method,  # HTTP method
                    "operation_id": operation_id,  # Unique operation ID
                    "request_body": request_body,  # Body parameter model reference
                    "request_params": request_model,  # Query/path parameter model reference
                    "responses": responses,  # Response models by status code
                    "description": self._format_markdown_tables(description),
                }
            )

            # Store mapping from operation ID to response models
            # This allows looking up responses by operation ID
            self.responses[operation_id] = responses
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(
                f"Error parsing Swagger 2.0 operation: {path} {method}", e
            )
            raise

    def _create_request_model(
        self, operation_id: str, parameters: List[Dict[str, Any]], path_template: str, method: str
    ) -> Optional[str]:
        """
        Create a model from operation parameters (query and path).

        This method processes operation parameters and creates a request parameter model.
        It extracts query and path parameters, as well as body parameters with proper references.

        For body parameters:
        1. It extracts referenced schema names
        2. It creates separate body models with a 'Body' suffix
        3. It ensures request models reference these body models properly
        4. It adds necessary imports for the referenced body schemas

        Args:
            operation_id: Operation ID.
            parameters: List of parameters.
            path_template: Path template (used to extract path parameters if not in parameters).

        Returns:
            Name of the created model, or None if no parameters found.
        """
        try:
            # Filter query and path parameters from the parameters list
            # This focuses only on parameters passed in query string or path
            # Body parameters are handled separately in the operation parsing methods
            request_params = [
                p for p in parameters if p.get("in") in ["query", "path", "body"]
            ]

            # Extract path parameters from the path template if they're not already in parameters
            # This handles cases where the path template contains parameters not explicitly defined
            # For example in path "/users/{userId}", we extract "userId" as a path parameter
            path_params_in_template = re.findall(r"\{([^}]+)\}", path_template)
            path_param_names = {
                p.get("name") for p in request_params if p.get("in") == "path"
            }

            # Add any path parameters found in the template but not already in the parameter list
            # This ensures all path parameters are included in the model even if not explicitly defined
            for path_param in path_params_in_template:
                if path_param not in path_param_names:
                    # Create a default parameter definition for missing path parameters
                    # Path parameters are always required for the API call to work
                    request_params.append(
                        {
                            "name": path_param,
                            "in": "path",
                            "required": True,  # Path parameters must be provided
                            "description": f"Path parameter: {path_param}",
                            "type": "string",  # Default to string type when not specified
                        }
                    )

            # If there are no parameters to process, return None (no model needed)
            # This happens when the operation doesn't require any query or path parameters
            if not request_params:
                return None

            # Create model name by converting operation ID to PascalCase and adding "Request" suffix
            # This follows naming convention for request parameter models
            # For example, "get_user" becomes "GetUserRequest"
            model_name = f"{self._create_first_letter_uppercase(operation_id)}Request"

            # Initialize collections to store property definitions and track required properties
            properties = {}  # Dictionary to hold all the model's properties
            required_props = []  # List to track which properties are required
            path_params = []
            # Process each parameter and convert it to a property in the model
            for param in request_params:
                name = param.get("name", "")  # Parameter name from the spec
                required = param.get("required", False)  # Whether parameter is required
                description = param.get("description", "")  # Parameter description
                param_location = param.get(
                    "in"
                )  # Where the parameter appears ('query' or 'path')

                # Special handling for array type parameters with enum values
                # This converts array enum parameters into properly typed list properties
                # (e.g., status_codes=[1, 2, 3] becomes List[StatusCodesEnum])
                schema = {}
                if (
                    param.get("type") == "array"
                    and "items" in param
                    and "enum" in param["items"]
                ):
                    # Create a schema object that can be processed by the _parse_property method
                    # This schema represents an array of enum values
                    schema = {
                        "type": "array",
                        "items": param["items"],  # Contains the enum values
                        "description": description,
                        "collectionFormat": param.get(
                            "collectionFormat", ""
                        ),  # How array items are formatted (csv, pipes, etc.)
                    }

                    # Copy additional enum metadata if available
                    # This preserves enum value descriptions and other extensions
                    # that provide more context for each enum value
                    if "x-docgen-enum-table-extension" in param["items"]:
                        schema["items"]["x-docgen-enum-table-extension"] = param[
                            "items"
                        ]["x-docgen-enum-table-extension"]
                # Handle different schema structures between Swagger 2.0 and OpenAPI 3.x
                elif "schema" in param:
                    # OpenAPI 3.x style - schema is in a dedicated field
                    # This is the modern approach for defining parameter schemas
                    schema = param.get("schema", {})
                else:
                    # Swagger 2.0 style - type info is directly in the parameter
                    # Create a schema-like structure for consistent processing
                    # This normalizes the older format to match the processing flow
                    schema = {
                        "type": param.get(
                            "type", "string"
                        ),  # Parameter type (default to string)
                        "format": param.get(
                            "format", ""
                        ),  # Format specification (e.g., date-time, uuid)
                        "description": description,  # Parameter description
                    }

                    # Handle enum values if present in Swagger 2.0 style
                    # Enums in Swagger 2.0 are directly in the parameter object
                    if "enum" in param:
                        schema["enum"] = param.get("enum", [])

                        # Copy enum documentation extensions if available
                        # These provide descriptions for each enum value
                        if "x-docgen-enum-table-extension" in param:
                            schema["x-docgen-enum-table-extension"] = param[
                                "x-docgen-enum-table-extension"
                            ]

                # Enhance description to indicate parameter location (query/path)
                # This makes it clear in the generated model where the parameter should be provided
                # and improves documentation for API users
                if description:
                    enhanced_description = re.sub('"', '"', f"[{param_location.upper()}] {description}")
                else:
                    enhanced_description = f"[{param_location.upper()}] Parameter"

                if param_location.upper() == "PATH":
                    path_params.append(name)
                # Parse the property using the existing property parsing method
                # This converts the parameter schema into a property definition
                # including type information, validation rules, and documentation
                snake_name = self.to_snake_case(
                    name
                )  # Convert to snake_case for Python compatibility
                properties[snake_name] = self._parse_property(name, schema, required, model_context=model_name)
                properties[snake_name][
                    "name"
                ] = name  # Preserve original parameter name for reference
                properties[snake_name][
                    "description"
                ] = enhanced_description  # Set enhanced description
                properties[snake_name][
                    "param_location"
                ] = param_location  # Store parameter location for template use

                # Handle default values if present in the parameter definition
                # This allows the generated model to provide sensible defaults
                if "default" in param:
                    properties[snake_name]["default"] = param["default"]

                    # For array enum types, ensure proper flags are set for template processing
                    # This handles the special case of default values for array enum parameters
                    if (
                        param.get("type") == "array"
                        and "items" in param
                        and "enum" in param["items"]
                    ):
                        properties[snake_name]["is_array"] = True  # Mark as array type
                        enum_name = self._create_unique_enum_name(
                            name, model_name
                        )
                        properties[snake_name][
                            "enum_name"
                        ] = enum_name  # Store enum name reference

                # Track required properties for model validation
                # Required properties will be marked in the Pydantic model
                if required:
                    required_props.append(name)

            # Create and store the complete model definition
            # This will be used by the generator to render the Pydantic model
            self.models[model_name] = {
                "name": model_name,  # Model class name
                "description": f"Request parameters for {operation_id}",  # Model description
                "properties": properties,  # Model properties dictionary
                "path_params": path_params,
                "method": method
            }

            # Store in request_params dictionary to track the relationship between
            # operation IDs and their request parameter models
            # This mapping is used later in the generator phase
            self.request_params[operation_id] = model_name

            # Return the name of the created model
            # This is used by the operation parsing methods to reference the model
            return model_name
        except Exception as e:
            # Handle any exceptions that occur during parsing
            # This provides better error diagnostics and allows for graceful failure
            self._handle_exception(
                f"Error creating request model for: {operation_id}", e
            )
            raise

    def _get_type(self, schema: Dict[str, Any]) -> str:
        """
        Get the type from a schema.

        Args:
            schema: Schema definition.

        Returns:
            Type string.
        """
        try:
            # Handle references
            if "$ref" in schema:
                return "ref"

            # Handle arrays
            if schema.get("type") == "array":
                return "array"

            # Handle objects
            if schema.get("type") == "object":
                return "object"

            # Handle basic types
            type_mapping = {
                "string": "string",
                "integer": "integer",
                "number": "number",
                "boolean": "boolean",
            }

            schema_type = schema.get("type", "string")
            schema_format = schema.get("format", "")

            # Special handling for string formats
            if schema_type == "string" and schema_format == "date-time":
                return "datetime"
            elif schema_type == "string" and schema_format == "date":
                return "date"
            elif schema_type == "string" and schema_format == "uuid":
                return "uuid"

            return type_mapping.get(schema_type, "string")
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception("Error getting type from schema", e)
            raise

    def _get_pydantic_type(self, type_str: str) -> str:
        """
        Convert a type string to a Pydantic type.

        Args:
            type_str: Type string.

        Returns:
            Pydantic type string.
        """
        try:
            type_mapping = {
                "string": "str",
                "integer": "int",
                "number": "float",
                "boolean": "bool",
                "object": "Dict[str, Any]",
                "datetime": "datetime",
                "date": "date",
                "uuid": "UUID",
            }

            return type_mapping.get(type_str, type_str)
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error getting Pydantic type for: {type_str}", e)
            raise

    def _get_ref_name(self, ref: str) -> str:
        """
        Get the model name from a reference.

        Args:
            ref: Reference string.

        Returns:
            Model name.
        """
        try:
            # Handle both Swagger 2.0 and OpenAPI 3.x references
            if ref.startswith("#/definitions/"):
                return ref.replace("#/definitions/", "")
            elif ref.startswith("#/components/schemas/"):
                return ref.replace("#/components/schemas/", "")
            else:
                return ref  # Default case for external references
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception(f"Error getting reference name: {ref}", e)
            raise

    def _create_first_letter_uppercase(self, name: str) -> str:
        """
        Convert a string to have the first letter uppercase, preserving camelCase or
        converting snake_case properly.

        Args:
            name: String to convert

        Returns:
            String with proper capitalization
        """
        if not name:
            return name

        # Handle snake_case: convert to PascalCase correctly
        if "_" in name:
            words = name.split("_")
            return "".join(word.capitalize() for word in words)

        # Handle camelCase: preserve existing casing but capitalize first letter
        elif any(c.isupper() for c in name[1:]) and not name.isupper():
            return name[0].upper() + name[1:]

        # Default: just capitalize first letter
        return name[0].upper() + name[1:]

    @staticmethod
    def to_snake_case(name: str) -> str:
        """
        Convert a string to snake_case.

        Args:
            name: String to convert

        Returns:
            snake_case version of the string
        """
        try:
            # Replace hyphens with underscores
            s1 = name.replace("-", "_")

            # Insert underscore before uppercase letters
            s2 = re.sub(r"([A-Z])", r"_\1", s1)

            # Convert to lowercase and remove leading underscore if present
            snake = s2.lower()
            if snake.startswith("_"):
                snake = snake[1:]

            # Replace any sequence of non-alphanumeric chars with a single underscore
            snake = re.sub(r"[^a-z0-9]+", "_", snake)

            return snake
        except Exception as e:
            print(f"Error in to_snake_case({name}): {str(e)}")
            raise

    @staticmethod
    def to_pascal_case(name: str) -> str:
        """
        Convert a string to PascalCase.

        Args:
            name: String to convert

        Returns:
            PascalCase version of the string
        """
        try:
            # Replace non-alphanumeric characters with underscores
            cleaned = re.sub(r"[^a-zA-Z0-9]", "_", name)

            # Split by underscores
            components = cleaned.split("_")

            # Join with all parts capitalized
            p = "".join(x[0].upper() + x[1:] for x in components if x)
            return p
        except Exception as e:
            print(f"Error in to_pascal_case({name}): {str(e)}")
            raise

    @staticmethod
    def _wrap_text(text, width=90, indent=8):
        """
        Wraps text to the specified width by adding newlines,
        but preserves table rows (lines starting with spaces and a |).

        Args:
            text: The text to wrap
            width: Maximum line length (default 90)

        Returns:
            Text with newlines inserted for wrapping
        """
        # Split the text into lines
        lines = text.split("\n")
        result = []
        matched_once = False

        for line in lines:
            # Check if the line is a table row (starts with spaces and a |)
            if re.match(r"^\s+\|", line):
                # Don't wrap table rows, add them as is
                result.append(line)
                matched_once = True
            else:
                if matched_once:
                    # Add a newline after the first non-table line
                    result.append("\n")
                    matched_once = False
                # For non-table lines, apply wrapping
                pattern = rf"(.{{1,{width}}})($)"
                wrapped = re.sub(pattern, rf"\1\n{' ' * indent}\2", line)
                # Add each wrapped line
                result.extend(wrapped.split("\n"))

        # Join all the lines back together
        return "\n".join(result)

    def _format_markdown_tables(self, text: str) -> str:
        """
        Extract and format markdown tables from text using tabulate.
        Works with various table formats.
        """
        # Find sequences of lines that start with | and contain at least one more |
        table_pattern = re.compile(r"((?:\|[^\n]*\|[ \t]*\n)+)", re.MULTILINE)

        def format_table(match):
            table_text = match.group(0)
            # Split into rows and filter empty lines
            rows = [
                line.strip()
                for line in table_text.split("\n")
                if line.strip() and "|" in line
            ]

            # Parse rows into columns
            parsed_rows = []
            for row in rows:
                # Strip leading/trailing | and split by |
                columns = [col.strip() for col in row.strip("|").split("|")]
                parsed_rows.append(columns)

            # Detect if there's a separator row (contains only -, :, or spaces)
            has_header = False
            if len(parsed_rows) > 1:
                second_row = "".join(parsed_rows[1])
                if re.match(r"^[\-: ]+$", second_row):
                    has_header = True

            if has_header:
                headers = parsed_rows[0]
                data = parsed_rows[2:]  # Skip the separator row
                return tabulate(data, headers=headers, tablefmt="github")
            else:
                # No header separator, just format as is
                return tabulate(parsed_rows, tablefmt="github")

        return re.sub(r'(\n\s*){2,}', '\n\n        ', self._wrap_text(
            re.sub("\n+", "\n        ", table_pattern.sub(format_table, text))
        ).rstrip())

    @staticmethod
    def _handle_exception(context: str, exception: Exception) -> None:
        """
        Handle exceptions with detailed error reporting.

        Args:
            context: Context information about where the error occurred
            exception: The exception that was raised
        """
        print(f"\nERROR: {context}")
        print(f"Exception: {type(exception).__name__}: {str(exception)}")
        print("\nStack trace:")
        traceback.print_exc(file=sys.stdout)
        print("\n")
