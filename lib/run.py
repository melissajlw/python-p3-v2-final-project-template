import ipdb

from cli import Cli
from sudoku import Sudoku
from player import Player

Sudoku.create_table()
Player.create_table()

cli = Cli()
cli.start()