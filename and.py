#!/usr/bin/env python3
import click

from commands.check import check
from commands.compile import compile
from commands.config import config
from commands.contest import contest
from commands.init import init
from commands.run import run

@click.group()
def ar():
    pass

ar.add_command(check)
ar.add_command(compile)
ar.add_command(config)
ar.add_command(contest)
ar.add_command(init)
ar.add_command(run)


if __name__ == "__main__":
    ar()
