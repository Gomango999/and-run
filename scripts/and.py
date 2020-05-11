#!/usr/bin/env python3
import click
import os
import datetime
import timeit

from constants import *
from files import *

@click.group()
def And():
    pass

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
@And.command()
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


# # Checks the done list to see if a problem is done or not
# def check_done(file):
#     done_list = root_dir() + "/build/done_list.txt"
#     with open(done_list, "r+") as f:
#         for line in f:
#             if file == line.strip():
#                 return True
#     return False

# # Mark a problem as complete
# @And.command()
# def done():
#     # Check if already completed
#     cwd = os.getcwd()
#     problem_name = os.path.basename(cwd)
#     if check_done(cwd):
#         print(f"Already completed {problem_name}")
#         return
#
#     # Not found, mark as complete
#     done_list = root_dir() + "/build/done_list.txt"
#     with open(done_list, "a") as f:
#         f.write(cwd + "\n")
#         print(f"{bcolors.OKGREEN}", end="")
#         print(f"✓ {problem_name} marked as completed")
#         print(f"{bcolors.ENDC}", end="")


# # Checks all the folders in the current directory, and
# # and displays which ones have been completed
# @And.command()
# def check():
#     cwd = os.getcwd()
#     files = next(os.walk(cwd))[1]
#     files.sort()
#
#     # Get stats
#     total = 0
#     completed = 0
#     for filename in files:
#         total += 1
#         if check_done(f"{cwd}/{filename}"):
#             completed += 1
#     if total == 0:
#         print("No folders in this directory")
#         exit(FAILED_CODE)
#
#     print(f"{bcolors.ENDC}", end="")
#     print(f"--------[Completed | {completed}/{total}]--------")
#
#     # List out files
#     for filename in files:
#         done = check_done(f"{cwd}/{filename}")
#         if done:
#             symbol = bcolors.OKGREEN + "✓"
#         else:
#             symbol = bcolors.FAIL + "✘"
#         print(f" {symbol} {filename}")

# Initialise a bunch of folders with alphabet letters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
@And.command()
@click.argument('letter', type=click.Choice(alphabet, case_sensitive=False), default="L")
def initletters(letter):
   letter = letter.upper()
   for ch in alphabet:
       exit_code = os.system(f"mkdir {ch}")
       if exit_code == SUCCESS_CODE:
           print(f"mkdir: {ch}: Successfully made")
       if ch == letter:
           break

@And.command()
@click.argument('type', type=click.Choice(["standard", "cases"], case_sensitive=False), default="standard")
def init(type):
    template_path = ""
    if (type == "standard"):
         template_path = root_dir() + "/config/templates/standard.cpp"
    if (type == "cases"):
         template_path = root_dir() + "/config/templates/cases.cpp"
    filename = get_basename() + ".cpp"
    if os.path.exists(os.path.join(os.getcwd(), filename)):
        print("File already exists")
        exit(FAILED_CODE)
    exit(os.system(f"cp {template_path} ./{filename}"))

if __name__ == "__main__":
    And()
