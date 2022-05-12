import click
import os
import string
import time


@click.command()
@click.argument('letter', 
    type=click.Choice(string.ascii_uppercase, case_sensitive=False), default="F")
def contest(letter):
    """ Initialise a series of folders labeled with alphabet letters
    """
    
    # Create folders up to the letter
    letter = letter.upper()
    for ch in string.ascii_uppercase:
        exit_code = os.system(f"mkdir {ch}")
        if exit_code == 0:
            print(f"mkdir: {ch}: Successfully made")
            
        # Stop when we reach the input letter
        if ch == letter:
            break
    
    # Create the notes document
    if not os.path.exists("notes.md"):
        exit_code = os.system(f"touch notes.md")
        if exit_code == 0:
            print(f"touch: notes.md: Successfully made")
            
            with open("notes.md", "w") as f:
                timenow = time.strftime("%-I:%M", time.localtime())
                f.write(f"{timenow} start\n")
                f.write("\n"*7)
                f.write("### Problems\n\n")
                for ch in string.ascii_uppercase:
                    f.write(f"{ch}. [] \n")
                    if ch == letter:
                        break
    else:
        print("touch: notes.md: File exists")
    
    
