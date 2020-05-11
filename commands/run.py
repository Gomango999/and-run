import click
import os
import timeit

import sys
sys.path.append('../')
from scripts.constants import *
from scripts.files import *

# Runs a script with nicely formatted printing
def pretty_run(input_file, cpp_file):
    cpp_filename, _ = os.path.splitext(cpp_file)
    print(f"--------[Input | {input_file}]--------")
    MAX_LINES = 10
    with open(input_file) as in_file:
        if file_len(input_file) > MAX_LINES:
            print(file_head(input_file, MAX_LINES), end="")
            print(f"... {file_len(input_file)-MAX_LINES} more lines")
        else:
            print(in_file.read(), end="")

    print(f"--------[Output | {cpp_file}]--------")
    start = timeit.default_timer()
    exit_code = os.system(f"./{cpp_filename} < {input_file}")
    stop = timeit.default_timer()
    run_time = stop-start

    if exit_code != SUCCESS_CODE:
        print("--------[Failed | {:.2}s]--------".format(run_time))
    else:
        print("--------[Done | {:.2}s]--------".format(run_time))
    exit_code

# Compiles and runs a cpp file
@click.command()
@click.option('-i', '--input', 'input_file', type=click.Path(exists=True, dir_okay=False), default=None)
@click.option('-f', '--file', 'cpp_file', type=click.Path(exists=True, dir_okay=False), default=None)
def run(input_file, cpp_file):
    if cpp_file == None:
        cpp_file = get_cpp_file()
    if cpp_file == None:
        print("No cpp file found")
        exit(FAILED_CODE)

    cpp_filename, _ = os.path.splitext(cpp_file)

    exit_code = os.system(f"g++ -o {cpp_filename} -std=c++17 -Wall {cpp_file}")
    if exit_code != SUCCESS_CODE:
        exit(exit_code);

    if input_file == None:
        input_file = get_input_file()
    if input_file == None:
        exit(os.system(f"./{cpp_filename}"))

    exit_code = pretty_run(input_file, cpp_file)
    exit(exit_code)
