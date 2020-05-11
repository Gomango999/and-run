import click
import os
import timeit
import time

import sys
sys.path.append('../')
from scripts.constants import *
from scripts.files import *

def print_fancy_bar(str):
    print(f"--------[{str}]--------")

# Runs a cpp file on an input file with nicely formatted printing
# Checks if output file has been updated recently, and if so, prints its contents out
MAX_LINES = 10 # Max number of lines of the input file to display
def pretty_run(input_filename, cpp_filename):
    cpp_fileroot, _ = os.path.splitext(cpp_filename)
    print_fancy_bar(f"Input | {input_filename}")
    with open(input_filename) as in_file:
        if file_len(input_filename) > MAX_LINES:
            print(file_head(input_filename, MAX_LINES), end="")
            print(f"... {file_len(input_filename)-MAX_LINES} more lines")
        else:
            print(in_file.read(), end="")

    print_fancy_bar(f"Output | {cpp_fileroot}")
    start_time = time.time()
    exit_code = os.system(f"./{cpp_fileroot} < {input_filename}")
    end_time = time.time()
    run_time = end_time-start_time

    #TODO: Check if most likely output file was modified. If so, print from that
    # Check if output file was modified recently. If so, then print from there
    output_filename = get_output_filename()
    if output_filename != None:
        last_modified = os.path.getmtime(output_filename)
        if (start_time <= last_modified <= end_time):
            # Wrote to output_file
            print(bcolors.CURSOR_UP_ONE, end="")
            print(bcolors.ERASE_LINE, end="")
            print_fancy_bar(f"Output | {cpp_filename} | {output_filename}")
            with open(output_filename) as out_file:
                print(out_file.read(), end="");


    if exit_code != SUCCESS_CODE:
        print_fancy_bar("Failed | {:.2}s".format(run_time))
    else:
        print_fancy_bar("Done | {:.2}s".format(run_time))
    exit_code

# Compiles and runs a cpp file
@click.command()
@click.option('-f', '--file', 'cpp_filename', type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-i', '--input', 'input_filename', type=click.Path(exists=True, dir_okay=False), default=None)
def run(cpp_filename, input_filename):
    if cpp_filename == None:
        cpp_filename = get_cpp_filename()
    if cpp_filename == None:
        print("No cpp file found")
        exit(FAILED_CODE)

    cpp_fileroot, _ = os.path.splitext(cpp_filename)

    exit_code = os.system(f"g++ -o {cpp_fileroot} -std=c++17 -Wall {cpp_filename}")
    if exit_code != SUCCESS_CODE:
        exit(exit_code);

    if input_filename == None:
        input_filename = get_input_filename()
    if input_filename == None:
        # Run on standard input and output
        exit(os.system(f"./{cpp_fileroot}"))
    else:
        # Run on input file
        exit_code = pretty_run(input_filename, cpp_filename)
        exit(exit_code)
