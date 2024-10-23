import ipdb

from game import Game
from cli import Cli
from sudoku import Sudoku

Game.create_table()

cli = Cli()
cli.start()