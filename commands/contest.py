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
        timenow = time.strftime("%-I:%M", time.localtime())
        exit_code = os.system(f"echo \"{timenow} start\" > notes.md")
        
        if exit_code == 0:
            print(f"touch: notes.md: Successfully made")
    else:
        print("touch: notes.md: File exists")
    
    
