import click
import os
import time

from commands.compile import check_and_compile_code
from config.config import config
from scripts.files import *
from scripts.helpers import *

def pretty_run(file_cpp, file_input):
    """ Runs a cpp file on an input file with nicely formatted printing
    - Checks if output file has been updated recently, and if so, prints its 
      contents out
    """
    
    print_fancy_bar(f" Input | {file_input} ")
    
    file_executable, _ = os.path.splitext(file_cpp)
    execute_command = ""
    
    if file_input:
        # Print first few lines of input (default = 10)
        os.system(f"head -n {config['input_lines']} {file_input}")
        print()
        
        # Print how many extra lines are in input
        file_len = get_file_len(file_input)
        if (file_len > config['input_lines']):
            print(GRAY, end="")
            extra = file_len - config['input_lines']
            s = "" if extra == 1 else "s"
            print(f"({extra} more line{s})") # probably bad style, but looks nice :)
            print(ENDC, end="")
        
        execute_command = f"./{file_executable} < {file_input}"
    else:
        # Just wait for user input
        execute_command = f"./{file_executable}"
    
    print_fancy_bar(f" Output | {file_executable} ")
    
    # Run the code and time it
    start_time = time.time()
    exit_code = os.system(execute_command)
    end_time = time.time()

    # Take a guess at the output file
    if file_input:
        file_output = inputfile_to_outputfile(file_input)
    else:
        file_outputs = get_output_filenames()
        if not file_outputs:
            file_output = None
        else:
            file_output = file_outputs[0]
        
    # Check to see if we should print from this output file (if it exists)
    if file_output and os.path.exists(file_output):
        last_modified = os.path.getmtime(file_output)
        if (start_time <= last_modified <= end_time):
            # Replace the previous bar
            print(CURSOR_UP, end="")
            print(ERASE_LINE, end="")
            print_fancy_bar(f" Output | {file_cpp} | {file_output} ")
            
            # Print the output file
            with open(file_output) as out_file:
                print(out_file.read(), end="");

    # Print out final bar, including runtime
    run_time = end_time-start_time
    status = "Done" if exit_code == 0 else "Failed"
    print_fancy_bar(f" {status} | {run_time:.3f}s ")
    
    return exit_code

def short_run(file_cpp, file_input):
    """ Runs a cpp file
    """
    file_executable, _ = os.path.splitext(file_cpp)
    exit_code = os.system(f"./{file_executable} < {file_input}")
    return exit_code

@click.command()
@click.argument('cpp_files', type=click.Path(exists=True, dir_okay=False), nargs=-1)
@click.option('-i', '--input', 'file_input', 
    type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-m', '--make', is_flag=True)
@click.option('-q', '--quiet', is_flag=True)
@click.option('-c', '--clean', is_flag=True)
def run(cpp_files, file_input, make, quiet, clean):
    """ Compiles and runs a cpp file
        - If no input file is specified, it will find the most likely input file
    """
    
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
    
    # Find a suitable input file
    if not file_input:
        file_inputs = get_input_filenames()
        if not file_inputs:
            file_input = None
        else:
            file_input = file_inputs[0]
    
    # Compile code if necessary
    check_and_compile_code(file_cpp, force=make)
        
    # Run the code   
    if quiet:
        exit_code = short_run(file_cpp, file_input)
    else:     
        exit_code = pretty_run(file_cpp, file_input)
        
    if clean:
        file_executable, _ = os.path.splitext(file_cpp)
        os.system(f"rm {file_executable}")
        
    exit(exit_code)
