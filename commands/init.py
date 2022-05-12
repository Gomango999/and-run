import click
import os
import subprocess

from config.config import config
from scripts.files import *
from scripts.helpers import *

@click.command()
@click.argument('file_cpp', type=str, default=None)
@click.option('-c', '--cases', is_flag=True)
@click.option('-l', '--light', is_flag=True)
def init(file_cpp, cases, light):
    """ Initialises a file to use
    """
    
    # Error checking
    if light and cases:
        print("Template can only be \"cases\" or \"light\", not both")
    
    # Work out file name
    if not file_cpp:
        file_cpp = get_basename() + ".cpp"
        
    if file_cpp[-4:] != ".cpp":
        print("Specified code file is not a C++ file")
        exit(1)
    
    # Get the template path
    template_type = ""
    if light:
        template_type = "light"
    elif cases:
        template_type = "cases"
    else:
        template_type = "standard"
    
    root = get_root_dir()
    template_path = template_paths[template_type]
    
    # If the file already exists, see if we can overwrite it
    if os.path.exists(os.path.join(os.getcwd(), file_cpp)):
        matched = False
        for path in template_paths.values():
            diff_command = f"diff -qw ./{file_cpp} {path}"
            diff_result = subprocess.getoutput(diff_command)
            if not diff_result:
                matched = True
                break
                
        if matched:
            print(f"{YELLOW}Warning{ENDC}: ", end="")
            print("Unmodified or empty file detected. Overwriting...")
        else:        
            # We have a modified file. It is not safe to modify
            print("Modified file already exists")
            exit(1)
        
    # Copy the template file
    exit_code = os.system(f"cp {template_path} ./{file_cpp}")
    if (exit_code == 0):
        print(f"Successfully made {file_cpp} using the \"{template_type}\" template")
    else:
        print("Creating code file from template failed")
        exit(1)
        
    # Create the input file
    exit_code = os.system(f"touch in.txt")
    if (exit_code == 0):
        print(f"Successfully made in.txt")

    exit(exit_code)

