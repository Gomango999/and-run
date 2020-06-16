#!/usr/bin/env python3
import click

from commands.run import run
from commands.initletters import initletters
from commands.init import init
from commands.edit import edit
# from commands.done import done
# from commands.check import check



@click.group()
def And():
    pass

And.add_command(run)
And.add_command(initletters)
And.add_command(init)
And.add_command(edit)
# And.add_command(done)
# And.add_command(check)

if __name__ == "__main__":
    And()
