from __init__ import CONN, CURSOR
from sudoku import Sudoku
import ipdb

class Player():

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError
        self._name = name

    def add_sudoku(self, sudoku):
        sudoku.player_id = self.id
        sudoku.save()

    def sudokus(self):
        from sudoku import Sudoku
        sql = '''
            SELECT * FROM sudokus
            WHERE sudokus.player_id = ?
        '''

        rows = CURSOR.execute(sql, (self.id,))
        return [Sudoku.create_by_row(row) for row in rows]

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT
            );
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE players;
        '''

        CURSOR.execute(sql)   

    @classmethod
    def create(cls, name):
        player = Player(name=name)
        player.save()
        return player
  
    @classmethod
    def find_by_id(cls, id):
        sql='''
            SELECT * FROM players
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return Player.create_by_row(row)
  
    @classmethod
    def all(cls):
        sql = '''
            SELECT * FROM players;
        '''

        players = CURSOR.execute(sql).fetchall()

        return [Player.create_by_row(row) for row in players]
  
    @classmethod
    def create_by_row(cls, row):
        return Player(id=row[0], name=row[1])

    @classmethod
    def delete_all(cls):
        for player in cls.all():
            player.delete()

    def save(self):
        if not self.id:
            sql = '''
                INSERT INTO players (name) VALUES (?)
            '''

            CURSOR.execute(sql, (self.name,))
            CONN.commit()

            sql = '''
                SELECT id FROM players ORDER BY id DESC LIMIT 1
            '''
            self.id = CURSOR.execute(sql).fetchall()[0][0]

        else:
            sql = '''
                UPDATE players SET name = ?
                WHERE id = ?
            '''

            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()

    def delete(self):
        sql = "DELETE FROM players WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def __repr__(self):
        return f'<Player id={self.id} name="{self.name}">'