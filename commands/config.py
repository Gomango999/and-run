import click
import os

import sys
sys.path.append('../')

from scripts.files import get_root_dir
from config.config import config

@click.command()
def config():
    root = get_root_dir()
    print(root)
    os.system(f"config['editor_command'] {root}")
    os.system(f"config['editor_command'] {root}/config/config.py")