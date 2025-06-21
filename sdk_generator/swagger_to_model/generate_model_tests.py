#!/usr/bin/env python3
import re
import sys
import inspect
import importlib.util
from pathlib import Path
from typing import get_origin, get_args, List, Dict, Union, Optional
from enum import Enum
from datetime import datetime

import click
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pydantic import BaseModel

# If your BaseModel is SpApiBaseModel, adjust this import:
# from your_package.common import SpApiBaseModel as BaseModel


TEMPLATE = """
# Auto-generated tests for {{ module_name }}.py
import pytest
from datetime import datetime
from {{ module_name }} import {{ importables | join(', ') }}

{% for cls in tests %}
def test_{{ cls.name.lower() }}_instantiates():
    \"\"\"Instantiate {{ cls.name }} with dummy data\"\"\"
    kwargs = {
    {%- for field in cls.fields %}
        "{{ field.name }}": {{ field.value }},
    {%- endfor %}
    }
    obj = {{ cls.name }}(**kwargs)
    assert isinstance(obj, {{ cls.name }})
{% endfor %}
"""


def load_module_from_path(path: Path):
    # Ensure package imports work by adding project root to sys.path
    # Find project root (parent directory containing the top-level package, e.g., 'sp_api')
    project_root = None
    for parent in path.parents:
        if (parent / "sp_api").is_dir():
            project_root = parent
            break
    if project_root is None:
        project_root = path.parent
    # Prepend project root to sys.path for imports
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    # Derive module name relative to project root, replacing path separators with dots
    rel_path = path.relative_to(project_root).with_suffix("")
    module_name = ".".join(rel_path.parts)

    # Load module with correct package context for relative imports
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    mod = importlib.util.module_from_spec(spec)
    # Set the package for relative imports
    mod.__package__ = module_name.rpartition(".")[0]
    spec.loader.exec_module(mod)
    return mod

def dummy_for_type(tp):
    origin = get_origin(tp)
    args = get_args(tp)

    # Optional[X] or Union[X, None]
    if origin is Union and type(None) in args:
        non_null = [a for a in args if a is not type(None)][0]
        return "None"

    # List[T]
    if origin in (list, List):
        return "[]"

    # Dict[K,V]
    if origin in (dict, Dict):
        return "{}"

    # Enum
    if inspect.isclass(tp) and issubclass(tp, Enum):
        member = list(tp)[0]
        return f"{tp.__name__}.{member.name}"

    # built-ins
    if tp is str:
        return "''"
    if tp is int:
        return "0"
    if tp is float:
        return "0.0"
    if tp is bool:
        return "False"

    # datetime: use a fixed sample datetime
    if tp is datetime:
        return "datetime(2000, 1, 1)"

    # Custom Pydantic models: instantiate nested models recursively
    if inspect.isclass(tp) and issubclass(tp, BaseModel):
        nested_kwargs = []
        for fname, fld in tp.model_fields.items():
            if fld.is_required:
                nested_val = dummy_for_type(fld.annotation)
                nested_kwargs.append(f"'{fname}': {nested_val}")
        return f"{tp.__name__}(**{{{', '.join(nested_kwargs)}}})"

    # fallback: zero-arg constructor
    if inspect.isclass(tp):
        return f"{tp.__name__}()"

    return "None"

def collect_test_data(module_path: Path):
    mod = load_module_from_path(module_path)
    # collect any Enum subclasses for import
    enums = [
        name for name, cls in vars(mod).items()
        if inspect.isclass(cls) and issubclass(cls, Enum) and cls is not Enum
    ]
    tests = []
    classes = []
    for name, cls in vars(mod).items():
        if inspect.isclass(cls) and issubclass(cls, BaseModel) and cls is not BaseModel:
            classes.append(name)
            fields = []
            for fname, fld in cls.model_fields.items():
                if fld.is_required:
                    tp = fld.annotation
                    val = dummy_for_type(tp)
                    fields.append({"name": fname, "value": val})
            tests.append({"name": name, "fields": fields})
    # combine models and enums for import
    importables = classes + enums
    import_name = re.sub('/', '.', re.sub(r'\.\./|\.py', '', str(module_path)))
    return {
        "module_name": import_name,
        "classes": classes,
        "enums": enums,
        "importables": importables,
        "tests": tests,
    }


def main(module_path: Path, output_path: Path):
    """
    Generate a pytest suite that instantiates every BaseModel in the given module.
    """
    data = collect_test_data(module_path)
    env = Environment(
        loader=FileSystemLoader(str(Path(__file__).parent)),
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    # use our inline template
    template = env.from_string(TEMPLATE)
    rendered = template.render(**data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    click.echo(f"✓ Wrote {len(data['tests'])} tests to {output_path}")
