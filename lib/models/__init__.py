import sqlite3

CONN = sqlite3.connect('db/sudoku.db')
CURSOR = CONN.cursor()
