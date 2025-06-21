"""
CLI for Swagger to Pydantic v2 models conversion.
"""

import os
import re
import sys
import traceback
import click
from urllib.parse import urlparse
from typing import Optional
from tqdm import tqdm

from swagger_to_model.get_tree import grouped
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


def generate(
    output_dir: str,
    client_dir: Optional[str] = None,
    template_dir: Optional[str] = None,
):
    """
    Generate Pydantic v2 models from a Swagger/OpenAPI specification.

    SWAGGER_SPEC can be a file path or URL to a Swagger/OpenAPI specification.
    """
    generator = None
    generated_clients = []
    for d, models in tqdm(list(grouped.items()), desc="Spec Groups", total=len(grouped)):
        directory = os.path.join(output_dir, d)
        clients_dir = os.path.join(client_dir, d)
        for model in tqdm(models, desc=f"Models in {d}", total=len(models), leave=False):
            swagger_spec = model['raw_link']
            if not swagger_spec.endswith((".json", ".yaml", ".yml")):
                generator = None
                continue
            try:
                # Create the parser
                parser = SwaggerParser()

                # Parse the specification
                parsed_data = parser.parse(swagger_spec)

                # Create the generator
                generator = ModelGenerator(d, template_dir)

                # Generate the models
                generator.generate_models(parsed_data, directory)


                # Generate the client if requested
                if clients_dir:
                    generated_clients.append(generator.generate_client(parsed_data, clients_dir))


            except Exception as e:
                click.echo(f"\nERROR: {str(e)}", err=True)
                click.echo("\nStack trace:", err=True)
                traceback.print_exc(file=sys.stderr)
                click.echo("\n", err=True)
                sys.exit(1)

        if generator is not None:
            generated_clients.extend(generator.generate_base_client([model['raw_link'] for model in models], clients_dir))

    generator.generate_api_init(output_dir, generated_clients)
    post_processor = PostProcessor(re.sub('models', '', output_dir))
    post_processor.run()

if __name__ == "__main__":
    generate(
        "../sp_api/api/models",
        "../sp_api/api/clients",
    )
