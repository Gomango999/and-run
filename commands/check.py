import click
import os

# Checks all the folders in the current directory, and
# and displays which ones have been completed
@click.command()
def check():
    cwd = os.getcwd()
    files = next(os.walk(cwd))[1]
    files.sort()

    # Get stats
    total = 0
    completed = 0
    for filename in files:
        total += 1
        if check_done(f"{cwd}/{filename}"):
            completed += 1
    if total == 0:
        print("No folders in this directory")
        exit(FAILED_CODE)

    print(f"{bcolors.ENDC}", end="")
    print(f"--------[Completed | {completed}/{total}]--------")

    # List out files
    for filename in files:
        done = check_done(f"{cwd}/{filename}")
        if done:
            symbol = bcolors.OKGREEN + "✓"
        else:
            symbol = bcolors.FAIL + "✘"
        print(f" {symbol} {filename}")
