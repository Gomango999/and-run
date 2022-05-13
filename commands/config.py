import click
import os

from scripts.files import get_root_dir
from config.config import config as _config # avoid confusion with function name

@click.command()
def config():
    root = get_root_dir()
    print(root)
    os.system(f"{_config['editor_command']} {root}")
    os.system(f"{_config['editor_command']} {root}/config/config.py")