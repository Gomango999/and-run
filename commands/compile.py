import click
import math
import os
import subprocess
import time

from config.config import config
from scripts.files import get_cpp_filenames
from scripts.helpers import *

def check_and_compile_code(file_cpp, force=False, erase=True):
    """ Checks if the code has been modified since the last time the executable
    has been run. 
        - If not, then we skip the compile step and print a warning
        - Otherwise, we compile the code, and print a message before deleting it
        - The force flag will force compilation no matter what
    """
    # If code has been modified, compile it again
    file_executable, _ = os.path.splitext(file_cpp)
    
    last_modified = time.localtime(os.path.getmtime(file_cpp))
    try:
        last_executed = time.localtime(os.path.getmtime(file_executable))
    except FileNotFoundError:
        last_executed = time.localtime(0)
        
    if (force or last_modified > last_executed):
        # Construct compile command
        cmd = f"{config['compiler']} -o {file_executable} {file_cpp} {config['flags']}"
        
        # Print the compile command to show user something is happening
        print(cmd)
        
        # Compile code
        exit_code = os.system(cmd)
        if exit_code != 0:
            exit(exit_code);
        
        # Remove the displayed compiled command
        #   This works for any terminal size. We work out the number of rows 
        #   based on the number of columns, and erase exactly enough lines.
        #   Will probably bug out if we resize the terminal during this step,
        #   but who does that?
        if erase:
            num_cols = int(subprocess.getoutput("tput cols"))
            num_rows_cmd = math.ceil((len(cmd)+1) / num_cols)
            for i in range(num_rows_cmd):
                print(CURSOR_UP, end=ERASE_LINE)
            print("\r", end="")
        
    else:
        # Did not compile again, since the code file has not changed
        print(f"{YELLOW}Warning{ENDC}: No changes to {file_cpp} since last compile")

@click.command()
@click.argument('cpp_files', type=click.Path(exists=True, dir_okay=False), nargs=-1)
@click.option('-f', '--force', is_flag=True)
def compile(cpp_files, force):
    
    if len(cpp_files) > 1:
        print("Cannot compile and run more than one C++ file")
        exit(1)
    elif len(cpp_files) == 0:
        # Find cpp files in directory
        cpp_files = get_cpp_filenames()
        if not cpp_files:
            print("Could not find a C++ file to compile")
            exit(1)
            
    file_cpp = cpp_files[0]
    
    if file_cpp[-4:] != ".cpp":
        print("Must specify a C++ file")
        exit(1)
        
    print(GRAY, end="")
    check_and_compile_code(file_cpp, force=force, erase=False)
    print(ENDC, end="")