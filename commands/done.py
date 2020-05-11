import click
import os

# Checks the done list to see if a problem is done or not
def check_done(file):
    done_list = root_dir() + "/build/done_list.txt"
    with open(done_list, "r+") as f:
        for line in f:
            if file == line.strip():
                return True
    return False

# Mark a problem as complete
@click.command()
def done():
    # Check if already completed
    cwd = os.getcwd()
    problem_name = os.path.basename(cwd)
    if check_done(cwd):
        print(f"Already completed {problem_name}")
        return

    # Not found, mark as complete
    done_list = root_dir() + "/build/done_list.txt"
    with open(done_list, "a") as f:
        f.write(cwd + "\n")
        print(f"{bcolors.OKGREEN}", end="")
        print(f"✓ {problem_name} marked as completed")
        print(f"{bcolors.ENDC}", end="")
