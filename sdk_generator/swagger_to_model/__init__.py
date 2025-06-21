"""
Swagger to Pydantic v2 Model Converter.

This package converts Swagger/OpenAPI specifications to Pydantic v2 models.
It handles special cases like using different base models for request models.
"""

from swagger_to_model.parser import SwaggerParser
from swagger_to_model.generator import ModelGenerator
from swagger_to_model.cli import cli

__version__ = "0.1.0"
__all__ = ["SwaggerParser", "ModelGenerator", "cli"]
