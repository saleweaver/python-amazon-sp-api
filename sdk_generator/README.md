# Swagger to Pydantic v2 Model Converter

This tool converts Swagger/OpenAPI specifications to Pydantic v2 models. It generates:

- Pydantic v2 models with proper typing and validation
- Special handling for request models (using `RequestsBaseModel`)
- API client code based on the Swagger/OpenAPI specification
- All using Jinja2 templates for easy customization

## Features

- Full support for Swagger 2.0 and OpenAPI 3.x specifications
- Load specifications from local files or URLs
- Automatic detection of request vs. response models
- Generation of proper Pydantic v2 model hierarchies
- Customizable templates for generating models and client code
- Command-line interface for easy usage
- Support for different base models for request models

## Installation

We use `uv` for Python package management:

```bash
# Install from the local directory in development mode
uv pip install -e .

# Or install the package directly
uv pip install .

# Install in a virtual environment
uv venv
source .venv/bin/activate  # On Unix/MacOS
# or
.venv\Scripts\activate     # On Windows
uv pip install -e .
```

## Usage

### Command Line Interface

```bash
# Basic usage with local file
swagger-to-model generate path/to/swagger.json

# Use a URL to a Swagger/OpenAPI specification
swagger-to-model generate https://petstore.swagger.io/v2/swagger.json

# Specify custom output directory
swagger-to-model generate path/to/swagger.json --output-dir ./my-models

# Generate models only (no client)
swagger-to-model generate path/to/swagger.json --no-client

# Specify custom template directory
swagger-to-model generate path/to/swagger.json --template-dir ./my-templates

# Specify client package name
swagger-to-model generate path/to/swagger.json --package-name my_api_client
```

### Programmatic Usage

```python
from swagger_to_model import SwaggerParser, ModelGenerator

# Parse the Swagger/OpenAPI specification from a file
parser = SwaggerParser("path/to/swagger.json")
parsed_data = parser.parse()

# Or parse from a URL
parser = SwaggerParser("https://petstore.swagger.io/v2/swagger.json")
parsed_data = parser.parse()

# Generate the models
generator = ModelGenerator()
generator.generate_models(parsed_data, "output/models")

# Generate the client
generator.generate_client(parsed_data, "output/client")
```

## Project Structure

The project uses a modern Python package structure with `pyproject.toml` for dependency management.

## Custom Templates

You can customize the generated code by providing your own Jinja2 templates. The following templates are used:

- `model.py.j2`: Template for model files
- `base_models.py.j2`: Template for base model classes
- `__init__.py.j2`: Template for model package `__init__.py` file
- `client.py.j2`: Template for API client
- `client_init.py.j2`: Template for client package `__init__.py` file

To use custom templates, specify the template directory when creating the `ModelGenerator`:

```python
generator = ModelGenerator(template_dir="path/to/templates")
```

Or use the `--template-dir` option with the CLI.

## Request vs. Response Models

The parser automatically detects which models are used for requests and which for responses. Models used for requests will inherit from `RequestsBaseModel` instead of the standard Pydantic `BaseModel`.

This allows you to apply special behavior to request models, such as different validation rules or serialization options.

## License

MIT
