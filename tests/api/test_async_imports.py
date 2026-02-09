import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_asyncio_api_package_imports_in_clean_process():
    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH")
    root_path = str(ROOT)
    env["PYTHONPATH"] = (
        f"{root_path}{os.pathsep}{existing_pythonpath}"
        if existing_pythonpath
        else root_path
    )
    result = subprocess.run(
        [sys.executable, "-c", "import sp_api.asyncio.api"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
