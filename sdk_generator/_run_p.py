import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from swagger_to_model.get_tree import grouped
from swagger_to_model.parser import SwaggerParser
from swagger_to_model.generator import ModelGenerator
from swagger_to_model.post_processor import PostProcessor
import os, traceback, click, sys

def process_model(d, model, output_dir, client_dir, template_dir):
    """Parse one spec and write its Pydantic models (and optional client)."""
    swagger_spec = model['raw_link']
    if not swagger_spec.endswith((".json", ".yaml", ".yml")):
        return None

    try:
        parser = SwaggerParser()
        parsed = parser.parse(swagger_spec)

        gen = ModelGenerator(d, template_dir)
        gen.generate_models(parsed, os.path.join(output_dir, d))

        if client_dir:
            client_path = os.path.join(client_dir, d)
            return gen.generate_client(parsed, client_path)
    except Exception as e:
        # bubble up so we can handle it in the main thread
        raise RuntimeError(f"[{d}] {swagger_spec} → {e}") from e

def generate(output_dir, client_dir=None, template_dir=None, max_workers=8):
    tasks = []
    for d, models in grouped.items():
        for model in models:
            tasks.append((d, model, output_dir, client_dir, template_dir))

    generated_clients = []
    with ThreadPoolExecutor(max_workers=max_workers) as exec:
        futures = {
            exec.submit(process_model, *t): t
            for t in tasks
        }
        for fut in as_completed(futures):
            try:
                client = fut.result()
                if client:
                    generated_clients.append(client)
            except Exception as err:
                click.echo(f"\nERROR: {err}", err=True)
                traceback.print_exc(file=sys.stderr)
                sys.exit(1)

    # generate a base client for each spec group
    if client_dir:
        for d, models in grouped.items():
            raw_links = [
                m['raw_link']
                for m in models
                if m['raw_link'].endswith((".json", ".yaml", ".yml"))
            ]
            if not raw_links:
                continue
            client_path = os.path.join(client_dir, d)
            gen = ModelGenerator(d, template_dir)
            generated_clients.extend(
                gen.generate_base_client(raw_links, client_path)
            )

    # now do the one-off steps
    # 1) if your ModelGenerator instance had shared state you’d need to handle it,
    #    but since we create a fresh one per task, you can safely do this here:
    if generated_clients:
        # Generate the API __init__.py using a ModelGenerator for the last group
        last_d = tasks[-1][0] if tasks else None
        last_gen = ModelGenerator(last_d, template_dir)
        last_gen.generate_api_init(output_dir, generated_clients)

    post = PostProcessor(re.sub('models', '', output_dir))
    post.run()
    # Clean tests folder
    post = PostProcessor('../tests')
    post.run()

if __name__ == "__main__":
    generate(
        "../sp_api/api/models",
        "../sp_api/api/clients",
        None,
        max_workers= min(32, os.cpu_count() * 2)  # tune to your SSD’s I/O capacity
    )