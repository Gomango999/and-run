import click
import os

import sys
sys.path.append('../')
from scripts.constants import *
from scripts.files import *

@click.command()
@click.option('-t', '--type', type=click.Choice(["standard", "cases"], case_sensitive=False), default="standard", show_default=True)
@click.argument('filename', type=str, default=None)
def init(type, filename):
    template_path = ""
    if (type == "standard"):
         template_path = root_dir() + "/config/templates/standard.cpp"
    if (type == "cases"):
         template_path = root_dir() + "/config/templates/cases.cpp"

    if filename == None:
        filename = get_basename() + ".cpp"

    if os.path.exists(os.path.join(os.getcwd(), filename)):
        print("File already exists")
        exit(FAILED_CODE)

    exit_code = os.system(f"cp {template_path} ./{filename}")
    if (exit_code == SUCCESS_CODE):
        print(f"Successfully created {filename} using the \"{type}\" template")
    else:
        print("Template initialisation failed")
    exit(exit_code)
