import click
import os

import sys
sys.path.append('../')

@click.command()
def edit():
    root = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    os.system(f"atom {root}")
