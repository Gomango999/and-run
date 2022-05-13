import click
import os

from scripts.files import get_root_dir

@click.command()
def edit():
    root = get_root_dir()
    print(root)
    os.system(f"atom {root}")