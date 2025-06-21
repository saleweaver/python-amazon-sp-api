import subprocess
import glob
import ast
from pathlib import Path
from collections import defaultdict


class PostProcessor:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def run(self) -> None:
        self.run_black(self.output_dir)
        self.run_isort(self.output_dir)

    def run_black(self, output_dir: str) -> None:

        try:

            paths = glob.glob(f"{output_dir}/**")
            subprocess.run(["black"] + paths, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running black formatter: {e}")

    def run_isort(self, output_dir: str) -> None:

        try:
            subprocess.run(["isort", output_dir], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running isort formatter: {e}")
