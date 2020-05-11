import click
import os

import sys
sys.path.append('../')
from scripts.constants import *

# Initialise a bunch of folders with alphabet letters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
@click.command()
@click.argument('letter', type=click.Choice(alphabet, case_sensitive=False), default="L")
def initletters(letter):
   letter = letter.upper()
   for ch in alphabet:
       exit_code = os.system(f"mkdir {ch}")
       if exit_code == SUCCESS_CODE:
           print(f"mkdir: {ch}: Successfully made")
       if ch == letter:
           break
