from __future__ import annotations

import argparse
import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import ast
from pathlib import Path
from typing import Set

marketplace_keys = ["marketplaceIds", "MarketplaceIds", "MarketplaceId", "MarketplaceIds", "marketplace_ids", "marketplaceIds", "marketplace_id", "marketplaceId"]


def rebase_to_request_model(py_file: Path):
    tree = ast.parse(py_file.read_text())
    # Filter out __future__ import nodes
    tree.body = [
        node for node in tree.body
        if not (isinstance(node, ast.ImportFrom) and node.module == '__future__')
    ]

    import_node = ast.ImportFrom(
        module="sp_api.base",
        names=[ast.alias(name="RequestBaseModel", asname=None)],
        level=0
    )
    class Rewriter(ast.NodeTransformer):
        def visit_ClassDef(self, node: ast.ClassDef):
            if node.name.endswith("Request") or node.name.endswith("Query"):

                # Replace the first base with RequestBaseModel.
                node.bases[0] = ast.Name(id="RequestBaseModel", ctx=ast.Load())

                has_model_config = any(
                    isinstance(stmt, ast.Assign) and
                    any(t.id == "model_config" for t in stmt.targets if isinstance(t, ast.Name))
                    for stmt in node.body
                )

                if not has_model_config:
                    config_node = ast.Assign(
                        targets=[ast.Name(id="model_config", ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Name(id="ConfigDict", ctx=ast.Load()),
                            args=[],
                            keywords=[
                                ast.keyword(arg="populate_by_name", value=ast.Constant(value=True))
                            ]
                        )
                    )
                    # Insert at the top of the class body
                    node.body.insert(0, config_node)
            return node

    new_tree = Rewriter().visit(tree)
    new_tree.body.insert(0, import_node)  # add the import at the top
    ast.fix_missing_locations(new_tree)
    py_file.write_text(ast.unparse(new_tree))
    subprocess.check_call([
        "black",
        "--line-length", "80",
        "--skip-magic-trailing-comma",
        "--force-exclude", "dummy",  # trick to ensure it processes
        str(py_file),

    ])


def swagger_to_openapi(swagger_path: Path) -> Path:
    """Return *Path* to a temporary OpenAPI3 file converted from *swagger_path*."""
    tmp_dir = Path(tempfile.mkdtemp())
    out_file = tmp_dir / "openapi.json"
    swagger_content = json.loads(swagger_path.read_text())
    for path, value in swagger_content.get("paths", {}).items():
        for verb, op in value.items():
            if verb not in ["get", "post", "put", "delete", "patch", "head", "options"]:
                continue
            for  param in op.get('parameters', []):
                if param.get('in') == 'query' and param.get('name') in marketplace_keys:
                    # Remove marketplace keys from query parameters
                    param['required'] = False
                if param.get('in') == 'path':
                    # Remove marketplace keys from path parameters
                    param['in'] = 'query'
                    param['description'] = "___SW_MOVED_TO_QUERY___" + param.get('description', '')

    for definition, value in swagger_content.get("definitions", {}).items():
        if value.get('required', []):
            value['required'] = [x for x in value.get('required', []) if x not in marketplace_keys]

    swagger_path.write_text(json.dumps(swagger_content, indent=4))
    # swagger2openapi has a small CLI we can re-use here so we don't need
    # to vendor any code.
    subprocess.check_call([

        "swagger2openapi",
        str(swagger_path),
        "-o",
        str(out_file),
        "--yaml",  # always force json -> yaml off (it flips automatically)
        "false",
    ])

    return out_file






######################################################################
# 2.  GENERATE CODE                                                   #
######################################################################
# We run datamodel-code-generator twice.  In the *first* run we only
# feed it the synthetic request models, therefore every generated class
# can safely derive from RequestBaseModel and include the helper
# request() method.  The *second* run contains everything else and
# sticks to pydantic.BaseModel so that we do not change response models.
######################################################################


def generate_models(swagger_path: Path, out: Path):

    tmp_spec = swagger_to_openapi(swagger_path)
    output_dir = out
    # 2. normal generation -------------------------------------------------
    template_dir = Path(__file__).with_suffix("").parent.parent / "templates"
    print(template_dir)
    "/Volumes/T7Touch/dev/programs/python-amazon-sp-api/templates"
    scopes = [
        "--openapi-scopes", *["schemas","paths","tags","parameters"]
    ]
    subprocess.check_call([
        "datamodel-codegen",
        "--input", str(tmp_spec),
        "--input-file-type", "openapi",
        "--output", str(output_dir / "models.py"),
        "--custom-template-dir", str(template_dir),
        "--field-constraints",
        "--allow-population-by-field-name",
        "--collapse-root-models",
        *scopes,
        "--use-operation-id-as-name",
        "--capitalise-enum-members",
        "--snake-case-field",
        "--formatters", "black",
        "--output-model-type", "pydantic_v2.BaseModel",
        "--target-python-version", "3.9",
        "--use-double-quotes",
        "--wrap-string-literal",
        "--disable-timestamp",
        # "--output-datetime-class", "datetime",
        "--field-include-all-keys",
        # "--field-include-all-keys"
    ])

    # rebase_to_request_model(out / 'models.py')



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("swagger", type=Path, help="Path to Swagger 2.0 file")
    parser.add_argument("out", type=Path, help="Directory for the generated python package")
    args = parser.parse_args()

    openapi_file = swagger_to_openapi(args.swagger)
    args.out.mkdir(parents=True, exist_ok=True)
    generate_models(openapi_file, args.out)
    print(f"✔︎ Models generated in {args.out}")


if __name__ == "__main__":
    main()
