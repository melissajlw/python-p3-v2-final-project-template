import helpers
from __init__ import CONN, CURSOR

class Sudoku():
    # Sudoku board generated defaults to easy mode
    def __init__(self, board="", difficulty="easy", player_id=None, id=None):
        if board == "NULL" or board == "" or not isinstance(board, str):
            sudoku_solution = helpers.generate_solved()
            sudoku_board = helpers.generate_unsolved(difficulty, sudoku_solution)
        else:
            sudoku_board = helpers.string_to_board(board)
            # print(f"This is the sudoku board {sudoku_board}")
            # print(f"This is the sudoku solution {sudoku_solution}")

        self.board = helpers.board_to_string(sudoku_board)
        self.difficulty = difficulty
        # self.completed = False
        self.player_id = player_id
        self.id = id

    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, board):
        if not isinstance(board, str) or not len(board) == 81 or not board.isnumeric():
            raise ValueError
        self._board = board
    
    def display(self):
        board = helpers.string_to_board(self.board)
        for row in range(len(board)):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - -")
            for col in range(len(board[0])):
                if col % 3 == 0 and col != 0:
                    print("| ", end = "")
                
                if col == 8:
                    print(board[row][col])
                else:
                    print(str(board[row][col]) + " ", end = "")
    
    def player(self):
        from player import Player
        sql = """
            SELECT * FROM players
            where id = ?
        """
        row = CURSOR.execute(sql, (self.player_id,)).fetchone()
        if row:
            return Player.create_by_row(row)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sudokus (
            id INTEGER PRIMARY KEY,
            board TEXT,
            difficulty TEXT,
            player_id INTEGER DEFAULT NULL
            );
        """

        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE sudokus;
        '''

        CURSOR.execute(sql)  

    @classmethod
    def create(cls, board="", difficulty="easy", player_id=None):
        sudoku = Sudoku(board=board, difficulty=difficulty, player_id=player_id)
        sudoku.save()
        return sudoku
    
    @classmethod
    def find_by_id(cls, id):
        sql='''
            SELECT * FROM sudokus
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return Sudoku.create_by_row(row)
    
    @classmethod
    def all(cls):
        sql = '''
            SELECT * FROM sudokus;
        '''

        sudokus = CURSOR.execute(sql).fetchall()

        return [Sudoku.create_by_row(row) for row in sudokus]

    @classmethod
    def create_by_row(cls, row):
        return Sudoku(id=row[0], board=row[1], difficulty=row[2], player_id=row[3])
    
    @classmethod
    def delete_all(cls):
        for sudoku in cls.all():
            sudoku.delete()

    def save(self):
        if not self.id:
            sql = '''
                INSERT INTO sudokus (board, difficulty, player_id) VALUES (?, ?, ?)
            '''

            CURSOR.execute(sql, (self.board, self.difficulty, self.player_id))
            CONN.commit()
            sql = '''
                SELECT id FROM sudokus ORDER BY id DESC LIMIT 1
            '''
            self.id = CURSOR.execute(sql).fetchall()[0][0]

        else:
            sql = '''
                UPDATE sudokus SET board = ?, difficulty = ?, player_id = ?
                WHERE id = ?
            '''

            CURSOR.execute(sql, (self.board, self.difficulty, self.player_id, self.id))
            CONN.commit()

    def delete(self):
        sql = "DELETE FROM sudokus WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    def unlink(self):
        sql = '''
            UPDATE sudokus SET player_id = NULL WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    def link_player(self, player):
        self.player_id = player.id
        self.save()
    
    def solve(self):
        solution = helpers.solve(helpers.string_to_board(self.board))
        solution_string = helpers.board_to_string(solution)
        self.board = solution_string
    
    def __repr__(self):
        return f'<Sudoku id={self.id} board="{self.board}" difficulty="{self.difficulty}" player_id={self.player_id}>'


# test_sudoku = Sudoku()
# test_sudoku.display()
# print(test_sudoku.board)

# test_sudoku_2 = Sudoku("123456789123456789123456789123456789123456789123456789123456789123456789123456789", "easy")
# test_sudoku_2.display()
# print(test_sudoku.board)
# for i in range(len(test_sudoku.board)):
#     row_list = test_sudoku.board[i]
#     row = ''.join(str(x) for x in row_list)
#     print(row)


"""
CLI
- main menu
    - enter player name
        - new sudoku game
            - easy 
                - new sudoku board
                - display the board
                    - solve
            - medium
                - new sudoku board
                - display the board
                    - solve
            - hard
                - new sudoku board
                - display the board
                    - solve
        - completed sudoku games
            - list sudoku games from db where player_name = foreign key 
            - select game
                - view 
                - delete
                - return to main menu


Tables 
- Player Table
    - id
    - name

- Games
    - id
    - mode (easy, medium, hard)
    - board_id
    - completed (true, false)
    - player_id

- Board
    - id
    - rows (row data)
    - columns (column data)
    - squares (square data)

- strings to parse

"""