import sqlite3

CONN = sqlite3.connect('sudoku.db')
CURSOR = CONN.cursor()
