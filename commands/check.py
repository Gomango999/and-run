import click
import os
import subprocess
import time

from commands.compile import check_and_compile_code
from config.config import config
from scripts.files import *
from scripts.helpers import *

@click.command()
@click.argument('file_cpp', type=click.Path(exists=True, dir_okay=False))
@click.option('-i', '--input', 'file_input', 
    type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-e', '--expected', 'file_expected', 
    type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-v', '--verbose', is_flag=True)
def check(file_cpp, file_input, file_expected, verbose):
    """ Checks the file against a series of inputs and outputs
        - Does not work for code that uses freopen to write to files
    """
    if file_cpp[-4:] != ".cpp":
        print("Must specify a C++ file")
        exit(1)
    
    if file_expected:
        if not file_input:
            print("Cannot specify an expected output file with a corresponding input file")
            exit(1)
    
    # Get all inputs to use for testing
    if file_input:
        input_filenames = [file_input]
    else:
        input_filenames = get_input_filenames()
        if not len(input_filenames):
            print("No input files found")
            exit(1)
            

    # Compile code if necessary
    check_and_compile_code(file_cpp)
    
    print_fancy_bar(f" {file_cpp} ")
    print(BOLD, end="")
    print(f"{'Input':16} {'Expected':16}    [   Status   ]")
    print(ENDC, end="")
    
    # Go through all input_filenames and run them
    file_executable, _ = os.path.splitext(file_cpp)
    
    for file_input in input_filenames:
        if file_expected:
            # User specified a custom expected output
            assert(len(input_filenames) == 1)
            output_filename = file_expected
        else:
            # Otherwise, guess the expected output file
            output_filename = inputfile_to_expectedfile(file_input)
            expected_output_exists = os.path.exists(output_filename)
            if not expected_output_exists:
                continue    
        
        # Run the code
        start_time = time.time()
        exit_code = os.system(f"./{file_executable} < {file_input} > tmp.out")
        end_time = time.time()
  
        # Work out the status of the program
        status = ""
        if exit_code != 0:
            status = "RE"
        else:
            # Program returned successfully, check it against expected
            diff_cmd = "diff -qw {} {}".format("tmp.out", output_filename)
            diff_result = subprocess.getoutput(diff_cmd)
            
            if not diff_result:
                status = "AC"
            else:
                status = "WA"
                # Print out the difference between the two
                diff_cmd = config["diff_command"].format("tmp.out", output_filename)
                os.system(diff_cmd)
        
        # Print the status line
        if status == "AC":   color = GREEN
        elif status == "WA": color = RED
        elif status == "RE": color = MAGENTA
        run_time = end_time - start_time
        in_out_part = f"{GRAY}< {file_input[:14]:14} > {output_filename[:14]:14}"
        status_part = f"{color}[ {status} | {run_time:.2f}s ]{ENDC}"
        status_line = in_out_part + " "*4 + status_part
        print(status_line)
            
    # Clean up files
    os.system("rm tmp.out")

