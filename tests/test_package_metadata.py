import runpy
from pathlib import Path
from unittest.mock import patch


def test_setup_requires_python_310_or_newer():
    setup_path = Path(__file__).parents[1] / "setup.py"

    with patch("setuptools.setup") as setup:
        runpy.run_path(str(setup_path), run_name="__main__")

    assert setup.call_args.kwargs["python_requires"] == ">=3.10"
