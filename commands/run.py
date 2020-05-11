import click
import os
import timeit

import sys
sys.path.append('../')
from scripts.constants import *
from scripts.files import *

# Runs a script with nicely formatted printing
MAX_LINES = 10 # Max number of lines of the input file to display
def pretty_run(input_file, cpp_file):
    cpp_filename, _ = os.path.splitext(cpp_file)
    print(f"--------[Input | {input_file}]--------")
    with open(input_file) as in_file:
        if file_len(input_file) > MAX_LINES:
            print(file_head(input_file, MAX_LINES), end="")
            print(f"... {file_len(input_file)-MAX_LINES} more lines")
        else:
            print(in_file.read(), end="")

    print(f"--------[Output | {cpp_file}]--------")
    start_time = timeit.default_timer()
    exit_code = os.system(f"./{cpp_filename} < {input_file}")
    stop_time = timeit.default_timer()
    run_time = stop_time-start_time

    if exit_code != SUCCESS_CODE:
        print("--------[Failed | {:.2}s]--------".format(run_time))
    else:
        print("--------[Done | {:.2}s]--------".format(run_time))
    exit_code

# Compiles and runs a cpp file
@click.command()
@click.option('-i', '--input', 'input_filename', type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-f', '--file', 'cpp_file', type=click.Path(exists=True, dir_okay=False), default=None)
def run(input_filename, cpp_filename):
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
