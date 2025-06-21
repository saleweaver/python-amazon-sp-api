"""
CLI for Swagger to Pydantic v2 models conversion.
"""

import os
import sys
import traceback
import click
from urllib.parse import urlparse
from typing import Optional

from swagger_to_model.parser import SwaggerParser
from swagger_to_model.generator import ModelGenerator
from swagger_to_model.post_processor import PostProcessor


def is_url(path_or_url: str) -> bool:
    """
    Check if a string is a valid URL.

    Args:
        path_or_url: String to check

    Returns:
        True if the string is a URL, False otherwise
    """
    parsed = urlparse(path_or_url)
    return bool(parsed.scheme and parsed.netloc)


@click.group()
def cli():
    """Convert Swagger/OpenAPI specifications to Pydantic v2 models."""
    pass


@cli.command()
@click.argument("swagger_spec", type=str)
@click.option(
    "-o",
    "--output",
    "output_dir",
    type=str,
    required=True,
    help="Directory where generated models will be saved.",
)
@click.option(
    "-c",
    "--client",
    "client_dir",
    type=str,
    help="Directory where generated client will be saved.",
)
@click.option(
    "-t",
    "--templates",
    "template_dir",
    type=str,
    help="Directory containing custom Jinja2 templates.",
)
def generate(
    swagger_spec: str,
    output_dir: str,
    client_dir: Optional[str] = None,
    template_dir: Optional[str] = None,
):
    """
    Generate Pydantic v2 models from a Swagger/OpenAPI specification.

    SWAGGER_SPEC can be a file path or URL to a Swagger/OpenAPI specification.
    """

    try:
        # Create the parser
        parser = SwaggerParser()
        module = swagger_spec.split("/")[-2].replace("-", "_").replace("_api_model", "")
        # Parse the specification
        click.echo(f"Parsing Swagger/OpenAPI specification from: {swagger_spec}")
        parsed_data = parser.parse(swagger_spec)

        # Create the generator
        generator = ModelGenerator(module, template_dir)

        # Generate the models
        click.echo(f"Generating Pydantic v2 models in: {output_dir}")
        generator.generate_models(parsed_data, output_dir)

        post_processor = PostProcessor(output_dir)
        post_processor.run()
        # Generate the client if requested
        if client_dir:
            click.echo(f"Generating API client in: {client_dir}")
            generator.generate_client(parsed_data, client_dir)
            generator.generate_base_client(parsed_data, client_dir)

        click.echo("Done!")

    except Exception as e:
        click.echo(f"\nERROR: {str(e)}", err=True)
        click.echo("\nStack trace:", err=True)
        traceback.print_exc(file=sys.stderr)
        click.echo("\n", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
