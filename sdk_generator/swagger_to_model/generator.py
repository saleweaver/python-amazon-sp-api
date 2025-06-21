"""
Generator module for Swagger to Pydantic v2 models.
"""
import itertools
import json
import keyword
import os
import re
import shutil
import subprocess
import traceback
import sys
from datetime import datetime
from itertools import chain
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from .generate_model_tests import main as gen_tests
import httpx
import jinja2


def to_uppercase_snake(text):
    """Convert any case style to UPPERCASE_SNAKE_CASE."""
    # First handle camelCase by adding underscores
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)

    # Then convert everything to uppercase
    return s2.upper().replace("-", "_").replace(" ", "_").replace(".", "_")


class ModelGenerator:
    """
    Generator for Pydantic v2 models from parsed Swagger/OpenAPI specification.

    This class is responsible for:
    1. Converting parsed Swagger/OpenAPI data into Pydantic v2 models
    2. Handling relationships between models, including body parameter models
    3. Managing enum definitions and their mapping to models
    4. Generating proper imports between model files
    5. Rendering models using Jinja2 templates
    """

    def __init__(self, module: str, template_dir: Optional[str] = None):
        """
        Initialize the generator with optional custom templates.

        This sets up the Jinja2 environment with templates and custom filters
        for code generation.

        Args:
            template_dir: Optional path to custom templates directory.
        """
        self.module = self._sanitize_module_name(module)

        try:
            # Set up Jinja2 environment
            if template_dir:
                self.template_loader = jinja2.FileSystemLoader(template_dir)
            else:
                default_templates = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "templates"
                )
                self.template_loader = jinja2.FileSystemLoader(default_templates)

            self.env = jinja2.Environment(
                loader=self.template_loader,
                trim_blocks=True,
                lstrip_blocks=True,
            )

            # Add custom filters - using lambda functions to properly define the filters
            self.env.filters["upper"] = lambda s: str(s).upper()
            self.env.filters["replace"] = lambda s, old, new: str(s).replace(old, new)
            self.env.filters["string"] = lambda s: str(s)
            self.env.filters["to_uppercase_snake"] = to_uppercase_snake
            self.env.filters["snake_case"] = self._to_snake_case
            self.env.filters["pascal_case"] = self._to_pascal_case
        except Exception as e:
            self._handle_exception("Error initializing ModelGenerator", e)
            raise

    def generate_models(self, parsed_data: Dict[str, Any], output_dir: str) -> None:
        """
        Generate Pydantic v2 models from parsed data.

        This is the main method that orchestrates the model generation process:
        1. Creates the output directory structure
        2. Groups models into appropriate modules
        3. Generates base models for inheritance
        4. Maps enums to their respective models
        5. Generates each model file with proper imports
        6. Generates request parameter models separately

        Body parameter models with a 'Body' suffix are handled specially to ensure
        they are referenced correctly in request models.

        Args:
            parsed_data: Data parsed from Swagger/OpenAPI specification.
            output_dir: Directory where generated models will be saved.
        """

        output_dir = output_dir + "/" + output_dir.split("/")[-1] + "_" + self._to_snake_case(
            parsed_data["client_version"])
        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Group models into modules
            modules = self._group_models_into_modules(parsed_data["models"])

            # Generate base models
            self._generate_base_models(output_dir)

            # Generate a package __init__.py
            self._generate_package_init(modules, output_dir)

            # Map enum classes to models
            model_enums = self._map_enums_to_models(parsed_data)

            # Generate each model file
            for module_name, module_models in modules.items():
                module_path = os.path.join(output_dir, f"{module_name}.py")

                # Skip empty modules
                if not module_models:
                    continue

                # Sort models by dependencies within the module
                sorted_module_models = self._sort_models_by_dependencies(
                    module_models, parsed_data["models"]
                )

                # Process each model for the template
                rendered_models = []
                for model_name in sorted_module_models:
                    model_data = parsed_data["models"][model_name]

                    # Include is_request_model flag
                    model_data["is_request_model"] = (
                            # model_name in parsed_data["request_models"]
                        False
                    )

                    # Include is_request_params flag
                    model_data["is_request_params"] = any(
                        model_name == rp_model
                        for rp_model in parsed_data.get("request_params", {}).values()
                    )

                    # Add enum definitions for this model if any
                    model_data["enums"] = model_enums.get(model_name, [])

                    rendered_models.append(self._render_model(model_data))

                # Write the module file
                with open(module_path, "w") as f:
                    imports = self._get_imports(
                        module_models, parsed_data["models"], modules
                    )
                    header = self._generate_module_header(module_name, imports, parsed_data['client_version'])

                    # Add model_rebuild() call at the end to resolve forward references
                    footer = "\n\n# Rebuild models to resolve forward references\n"
                    footer += "\n".join(
                        [
                            x + ".model_rebuild()"
                            for x, y in parsed_data["models"].items()
                            if x in module_models
                            and "is_array" not in y
                            and "is_primitive" not in y
                        ]
                    )

                    f.write(header + "\n\n" + "\n\n".join(rendered_models) + footer)

            gen_tests(Path(output_dir + '/common.py'), Path('../tests/models/' + re.sub('../sp_api/api/models', '', output_dir) + f'/test_{output_dir.split("/")[-1]}_common.py'))
        except Exception as e:
            self._handle_exception("Error generating models", e)
            raise

    def _parse_version(self, swagger_url: str):
        """
        Parse version from swagger url
        :param swagger_url:
        :return str:
        """

        try:
            # Make HTTP request to get the swagger spec
            response = httpx.get(swagger_url)  # Use httpx for HTTP requests
            response.raise_for_status()  # Raise exception for non-200 responses
            swagger_spec = json.loads(response.text)

            version = swagger_spec.get("info", {}).get("version", "0")
            return version
        except Exception as e:
            # Handle any exceptions that occur during parsing
            self._handle_exception("Error parsing Swagger/OpenAPI specification", e)
            raise

    def generate_base_client(self, group_clients_swagger_json: List[str], output_dir: str) -> List[Dict[str, Any]]:
        """
        Generate base client from parsed data.

        Args:
            parsed_data: Data parsed from Swagger/OpenAPI specification.\
            group_clients_swagger_json: List of swagger json files for group clients
            output_dir: Directory where generated client will be saved.
        """

        def sort_versions(versions):
            def sort_key(v):
                if v.startswith('v'):
                    # Extract numeric part from 'v0', 'v1', etc.
                    try:
                        return 0, int(re.sub(r'\D', '', v))
                    except ValueError:
                        return 0, float('inf')  # Put malformed 'v' entries at the end of 'v' group
                else:
                    # Parse date: '2024_06_01' → (1, datetime(...))
                    try:
                        dt = datetime.strptime(v, '%Y_%m_%d')
                        return 1, dt
                    except ValueError:
                        return 2, v  # Unknown format, push to end

            return sorted(versions, key=sort_key)

        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            versions = [self._parse_version(swagger_url) for swagger_url in group_clients_swagger_json]
            versions = sort_versions(versions)
            template = self.env.get_template("base_client.py.j2")
            output_path = os.path.join(output_dir, "base_client.py")
            pyi_template = self.env.get_template("base_client.pyi.j2")
            pyi = os.path.join(output_dir, "base_client.pyi")
            with open(output_path, "w") as f:
                f.write(
                    template.render(
                        versions=versions,
                        module=self.module,
                    )
                )
            with open(pyi, 'w') as f:
                f.write(
                    pyi_template.render(versions=versions, module=self.module)
                )
            return [{
                "module": f"clients.{self.module}.base_client", "name": self._to_pascal_case(self.module)
            }, {
                "module": f"clients.{self.module}.base_client", "name": f"{self._to_pascal_case(self.module)}Version"
            }]
        except Exception as e:
            # Handle any exceptions that occur during generation
            self._handle_exception("Error generating base client", e)
            raise

    def generate_api_init(self, output_dir: str, generated_clients: List[Dict[str, Any]]) -> None:
        try:
            template = self.env.get_template("api_init.py.j2")
            output_path = os.path.join(re.sub('models', '', output_dir), "__init__.py")

            with open(output_path, "w") as f:
                f.write(
                    template.render(
                        imports=generated_clients,
                    )
                )
        except Exception as e:
            self._handle_exception("Error generating api init", e)
            raise

    def generate_client(
            self, parsed_data: Dict[str, Any], output_dir: str, package_name: str = "client"
    ) -> Dict[str, Any]:
        """
        Generate API client from parsed data.

        Args:
            parsed_data: Data parsed from Swagger/OpenAPI specification.
            output_dir: Directory where generated client will be saved.
            package_name: Name of the client package.
        """
        try:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Extract and prepare operations for the client template
            operations = []

            # Process the paths to extract operations
            endpoints = parsed_data.get("endpoints", {})

            template = self.env.get_template("client.py.j2")
            output_path = os.path.join(output_dir, f"{self.module}_v_{self._to_snake_case(parsed_data['client_version'])}.py")
            client_name = f'{self._to_pascal_case(self.module)}_V_{self._to_snake_case(parsed_data["client_version"])}'

            with open(output_path, "w") as f:
                f.write(
                    template.render(
                        endpoints=endpoints,
                        title=parsed_data["client_title"],
                        description=parsed_data["client_description"],
                        version=parsed_data["client_version"],
                        module=self.module,
                    )
                )

            # Generate __init__.py
            template = self.env.get_template("client_init.py.j2")
            output_path = os.path.join(output_dir, "__init__.py")

            with open(output_path, "w") as f:
                f.write(template.render(package_name=package_name))

            return {"module": f"clients.{self.module}.{self.module}_v_{self._to_snake_case(parsed_data['client_version'])}", "name": client_name}



        except Exception as e:
            self._handle_exception("Error generating client", e)
            raise

    def _generate_module_header(
            self, module_name: str, imports: List[Dict[str, str]], version: str
    ) -> str:
        """
        Generate header for a model module.

        Args:
            module_name: Name of the module.
            imports: List of import dictionaries.

        Returns:
            Header string for the module.
        """
        try:
            header = f'"""\n{module_name.title()} models generated from Swagger/OpenAPI specification.\n\nThis file was auto-generated. Do not edit manually.\n\n"""\n\n'
            header += "from typing import Any, Dict, List, Optional, Union, Annotated\n"
            header += "from datetime import datetime, date\n"
            header += "from uuid import UUID\n"
            header += "from enum import Enum, auto\n"
            header += (
                "from pydantic import Field, ConfigDict, AliasChoices\n\n"
            )
            header += "from .base_models import RequestsBaseModel, SpApiBaseModel, GetRequestSerializer, PathParam, BodyParam, QueryParam\n"

            # Add imports for referenced models

            for import_item in imports:
                if import_item.get('custom', False):
                    header += f"from {import_item['module']} import {import_item['name']}\n"
                else:
                    header += f"from {import_item['module']} import {import_item['name']}\n"
            header += "\n"
            # Import base models
            header += f"from .base_models import RequestsBaseModel\n"

            return header
        except Exception as e:
            self._handle_exception("Error generating module header", e)
            raise

    def _to_snake_case(self, name: str) -> str:
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
            print(f"Error in _to_snake_case({name}): {str(e)}")
            raise

    def _to_camel_case(self, name: str) -> str:
        """
        Convert a string to camelCase.

        Args:
            name: String to convert

        Returns:
            camelCase version of the string
        """
        try:
            # Split by underscores or dashes
            components = re.split(r"[_-]", name)

            # Join with first part lowercase and rest capitalized
            return components[0].lower() + "".join(x.title() for x in components[1:])
        except Exception as e:
            print(f"Error in _to_camel_case({name}): {str(e)}")
            raise

    def _to_pascal_case(self, name: str) -> str:
        """
        Convert a string to PascalCase.

        Args:
            name: String to convert

        Returns:
            PascalCase version of the string
        """
        try:
            # Split by underscores or dashes
            components = re.split(r"[_-]", name)

            # Join with all parts capitalized
            return "".join(x.title() for x in components)
        except Exception as e:
            print(f"Error in _to_pascal_case({name}): {str(e)}")
            raise

    def _handle_exception(self, context: str, exception: Exception) -> None:
        """
        Handle exceptions with detailed error reporting.

        Args:
            context: Context information about where the error occurred
            exception: The exception that was raised
        """
        print(f"\nERROR: {context}: {str(exception)}")
        traceback.print_exc(file=sys.stdout)
        print("\n")

    def _add_enum_imports(self, model_data: Dict[str, Any], imports: Set[str]) -> None:
        """
        Add necessary enum imports to the imports set.

        This method identifies which enums are used by the model and adds
        the necessary import statements to the provided imports set.

        Args:
            model_data: Model data containing properties that may use enums.
            imports: Set of import statements to update.
        """
        try:
            # Add enum import if model has enum properties
            if model_data.get("enums"):
                # Add the enum module import if not already present
                imports.add("from enum import Enum")

            # Check properties for array types with enum values
            for prop_name, prop in model_data.get("properties", {}).items():
                # Handle array properties with enum types
                if prop.get("is_array") and prop.get("enum_name"):
                    # Enums in arrays need special handling for default values
                    imports.add("from enum import Enum")
                # Also check for referenced models in older property format
                elif prop.get("type") == "ref" and "ref" in prop:
                    # Enums in refs need special handling for default values
                    imports.add("from enum import Enum")
                # Handle array of refs in older format
                elif (
                        prop.get("type") == "array"
                        and prop.get("items", {}).get("type") == "ref"
                ):
                    ref = prop.get("items", {}).get("ref")
                    if ref in model_data["properties"]:
                        imports.add("from enum import Enum")
        except Exception as e:
            # Handle any exceptions that occur while processing enum imports
            self._handle_exception("Error adding enum imports", e)
            raise

    def _render_model(self, model_data: Dict[str, Any]) -> str:
        """
        Render a model using the Jinja2 template.

        This method applies the model data to the Jinja2 template to generate
        the Python code for the model. It handles:
        - Basic model properties
        - Enum definitions
        - Special handling for body parameters
        - Import references

        Args:
            model_data: Dictionary with model definition and properties.

        Returns:
            String containing the rendered model as Python code.
        """
        try:
            # Prepare imports for this specific model
            # These are imports that will be rendered within the template
            imports = []

            # If the model has properties, process them for rendering
            if "properties" in model_data:
                for prop_name, prop in model_data["properties"].items():
                    # Handle body parameter references
                    # If a property is a body reference, ensure it references the correct model
                    if prop.get("is_body_reference") and prop.get("reference_name"):
                        # For body references, import the referenced model
                        # This ensures proper typing in the generated code
                        ref_name = prop["reference_name"]

                        # Add imports for the referenced body model
                        # This handles both single references and list/array references
                        module = "common"  # Default module for most models
                        imports.append({"module": module, "name": ref_name, 'custom': True})

            # Render the model using the Jinja2 template
            # Pass model data and imports to the template for rendering
            return self.env.get_template("model.py.j2").render(
                model=model_data, imports=imports
            )
        except Exception as e:
            # Handle any exceptions that occur during template rendering
            self._handle_exception(
                f"Error rendering model: {model_data.get('name', 'unknown')}", e
            )
            raise

    def _group_models_into_modules(
            self, models: Dict[str, Dict[str, Any]]
    ) -> Dict[str, List[str]]:
        """
        Group models into modules based on naming conventions.

        Args:
            models: Dictionary of models from parsed data.

        Returns:
            Dictionary mapping module names to lists of model names.
        """
        try:
            modules = {"common": []}

            for model_name in models:
                modules['common'].append(model_name)
                # Try to extract a module name from the model name
                # Common patterns like User_Profile, UserProfile, User.Profile
                # parts = re.split(r"[_.]", model_name)
                # if len(parts) > 1:
                #     # Use the first part as a potential module name
                #     module_name = self._sanitize_module_name(self._to_snake_case(parts[0]))
                # else:
                #     # Try to extract from camelCase or PascalCase
                #     match = re.match(r"^([A-Z][a-z]+)", model_name)
                #     if match:
                #         module_name = self._sanitize_module_name(self._to_snake_case(match.group(1)))
                #     else:
                #         # Default to common module
                #         module_name = "common"
                #
                # # Initialize the module if it doesn't exist
                # if module_name not in modules:
                #     modules[module_name] = []
                #
                # # Add the model to the module
                # modules[module_name].append(model_name)

            return modules
        except Exception as e:
            self._handle_exception("Error grouping models into modules", e)
            raise

    def _generate_base_models(self, output_dir: str) -> None:
        """
        Generate base model classes.

        Args:
            output_dir: Directory where generated models will be saved.
        """
        try:
            template = self.env.get_template("base_models.py.j2")
            output_path = os.path.join(output_dir, "base_models.py")

            with open(output_path, "w") as f:
                f.write(template.render())
        except Exception as e:
            self._handle_exception("Error generating base models", e)
            raise

    def _generate_package_init(
            self, modules: Dict[str, List[str]], output_dir: str
    ) -> None:
        """
        Generate __init__.py for the models package.

        Args:
            modules: Dictionary mapping module names to lists of model names.
            output_dir: Directory where generated models will be saved.
        """
        try:
            template = self.env.get_template("__init__.py.j2")
            output_path = os.path.join(output_dir, "__init__.py")

            with open(output_path, "w") as f:
                f.write(template.render(modules=modules,
                                        all_entries=list(itertools.chain(chain.from_iterable(modules.values())))))
        except Exception as e:
            self._handle_exception("Error generating package __init__.py", e)
            raise

    def _get_imports(
            self,
            model_names: List[str],
            all_models: Dict[str, Dict[str, Any]],
            modules: Dict[str, List[str]],
    ) -> List[Dict[str, str]]:
        """
        Get imports needed for a module.

        Args:
            model_names: List of model names in the current module.
            all_models: Dictionary of all models from parsed data.
            modules: Dictionary mapping module names to lists of model names.

        Returns:
            List of import dictionaries with module and name keys.
        """
        try:
            imports = []
            referenced_models = set()

            # Add standard imports
            imports.append(
                {"module": "typing", "name": "Any, Dict, List, Optional, Union"}
            )
            imports.append({"module": "datetime", "name": "datetime, date"})
            imports.append({"module": "uuid", "name": "UUID"})
            imports.append(
                {"module": "pydantic", "name": "BaseModel, Field, ConfigDict"}
            )

            # Collect referenced models
            for model_name in model_names:
                model = all_models[model_name]
                for prop in model["properties"].values():
                    # Handle reference types
                    if prop["type"] == "model":
                        referenced_models.add(prop["model_name"])
                    # Handle array types safely
                    elif prop["type"] == "array":
                        if "item_type" in prop and prop["item_type"] == "model":
                            referenced_models.add(prop["model_name"])
                        # For backwards compatibility with older code
                        elif "items" in prop and prop["items"].get("type") == "ref":
                            referenced_models.add(prop["items"]["ref"])
                    # Also check for referenced models in older property format
                    elif prop["type"] == "ref" and "ref" in prop:
                        referenced_models.add(prop["ref"])
                    # Handle array of refs in older format
                    elif (
                            prop.get("type") == "array"
                            and prop.get("items", {}).get("type") == "ref"
                    ):
                        ref = prop.get("items", {}).get("ref")
                        if ref in model_names:
                            referenced_models.add(ref)

            # Remove models that are in the current module
            referenced_models = referenced_models - set(model_names)

            # Map referenced models to their modules
            for ref_model in referenced_models:
                for module_name, module_models in modules.items():
                    if ref_model in module_models:
                        imports.append({"module": f".{module_name}", "name": ref_model, 'custom': True})
                        break

            return imports
        except Exception as e:
            self._handle_exception("Error getting imports", e)
            raise


    def _sort_models_by_dependencies(
            self, model_names: List[str], all_models: Dict[str, Dict[str, Any]]
    ) -> List[str]:
        """
        Sort models by dependencies to ensure classes are defined before they are used.

        Args:
            model_names: List of model names to sort.
            all_models: Dictionary of all models from parsed data.

        Returns:
            Sorted list of model names.
        """
        try:
            # Build the dependency graph
            # Key is model name, value is set of model names it depends on
            dependency_graph = {name: set() for name in model_names}

            # Collect dependencies from properties
            for model_name in model_names:
                model = all_models[model_name]
                for prop in model.get("properties", {}).values():
                    # Handle direct model references
                    if (
                            prop.get("type") == "model"
                            and prop.get("model_name") in model_names
                    ):
                        dependency_graph[model_name].add(prop["model_name"])
                    # Handle array of models
                    elif (
                            prop.get("type") == "array" and prop.get("item_type") == "model"
                    ):
                        if prop.get("model_name") in model_names:
                            dependency_graph[model_name].add(prop["model_name"])
                    # For backwards compatibility with older property format
                    elif prop.get("type") == "ref" and prop.get("ref") in model_names:
                        dependency_graph[model_name].add(prop["ref"])
                    # Handle array of refs in older format
                    elif (
                            prop.get("type") == "array"
                            and prop.get("items", {}).get("type") == "ref"
                    ):
                        ref = prop.get("items", {}).get("ref")
                        if ref in model_names:
                            dependency_graph[model_name].add(ref)

            # Perform topological sort
            # Start with nodes that have no dependencies (leaves of the graph)
            sorted_models = []
            temp_marks = set()  # For cycle detection
            perm_marks = set()  # Models already sorted

            def visit(node):
                """Visit node in depth-first search."""
                if node in perm_marks:
                    return
                if node in temp_marks:
                    # Circular dependency detected - break the cycle
                    # We'll just continue as if it's already sorted
                    return

                temp_marks.add(node)

                # Visit all dependencies first
                for dep in sorted(
                        dependency_graph[node]
                ):  # Sort for deterministic output
                    visit(dep)

                # After all dependencies are visited, add this node
                temp_marks.remove(node)
                perm_marks.add(node)
                sorted_models.append(node)

            # Visit all nodes
            for node in sorted(model_names):  # Sort for deterministic initial ordering
                if node not in perm_marks:
                    visit(node)

            return sorted_models
        except Exception as e:
            self._handle_exception("Error sorting models by dependencies", e)
            # In case of error, return original list to be safe
            return model_names

    def _map_enums_to_models(
            self, parsed_data: Dict[str, Any]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Map enum definitions to their corresponding models.

        This method:
        1. Iterates through all models to find properties with enum types
        2. Looks up the corresponding enum definition
        3. Collects and organizes enum definitions by model
        4. Includes request parameter models in the mapping

        This ensures that models with enum properties will have access to the enum
        definitions when they're rendered.

        Args:
            parsed_data: Data parsed from Swagger/OpenAPI specification.

        Returns:
            Dictionary mapping model names to lists of enum definitions they use.
        """
        try:
            result = {}

            # Get all enum definitions
            all_enums = parsed_data.get("enums", {})

            # Map models to their enum definitions
            for model_name, model_data in parsed_data["models"].items():
                enum_defs = []

                for prop_name, prop in model_data["properties"].items():
                    if prop["type"] == "enum":
                        enum_name = prop.get("enum_name")
                        if enum_name and enum_name in all_enums:
                            enum_def = all_enums[enum_name].copy()

                            # Ensure consistent key name for enum values
                            if "values" in enum_def and "enum_values" not in enum_def:
                                enum_def["enum_values"] = enum_def.pop("values")
                            elif "enum_values" not in enum_def:
                                enum_def["enum_values"] = prop.get("enum_values", [])

                            if not any(e["name"] == enum_name for e in enum_defs):
                                enum_defs.append(enum_def)

                if enum_defs:
                    result[model_name] = enum_defs

            # Also check request parameter models for enums
            for operation_id, model_name in parsed_data.get(
                    "request_params", {}
            ).items():
                if model_name in parsed_data["models"] and model_name not in result:
                    model_data = parsed_data["models"][model_name]
                    enum_defs = []

                    for prop_name, prop in model_data["properties"].items():
                        if prop["type"] == "enum":
                            enum_name = prop.get("enum_name")
                            if enum_name and enum_name in all_enums:
                                enum_def = all_enums[enum_name].copy()

                                # Ensure consistent key name for enum values
                                if (
                                        "values" in enum_def
                                        and "enum_values" not in enum_def
                                ):
                                    enum_def["enum_values"] = enum_def.pop("values")
                                elif "enum_values" not in enum_def:
                                    enum_def["enum_values"] = prop.get(
                                        "enum_values", []
                                    )

                                if not any(e["name"] == enum_name for e in enum_defs):
                                    enum_defs.append(enum_def)

                    if enum_defs:
                        result[model_name] = enum_defs

            return result
        except Exception as e:
            self._handle_exception("Error mapping enums to models", e)
            raise

    def _sanitize_module_name(self, name: str) -> str:
        """
        If `name` is a Python keyword, append '_module'.
        Otherwise return it unchanged (also convert invalid chars to underscores).
        """
        # First, make it a valid identifier: replace non-alphanumeric/_ with _
        safe = re.sub(r'[^0-9a-zA-Z_]', '_', name)
        # Ensure it doesn’t start with a digit
        if re.match(r'^\d', safe):
            safe = '_' + safe

        # Finally, avoid keywords
        if keyword.iskeyword(safe):
            safe += '_module'

        return safe