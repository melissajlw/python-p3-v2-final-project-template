import generate_board

class Sudoku():
    # Sudoku board generated defaults to easy mode
    def __init__(self, difficulty="easy"):
        sudoku_solution = generate_board.generate_solved()
        sudoku_board = generate_board.generate_unsolved(difficulty, sudoku_solution)
        self.board = sudoku_board
        self.solution = sudoku_solution
        self.difficulty = difficulty
        self.completed = False
    
    def display(self):
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - -")
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("| ", end = "")
                
                if col == 8:
                    print(self.board[row][col])
                else:
                    print(str(self.board[row][col]) + " ", end = "")

test_sudoku = Sudoku()
test_sudoku.display()
print(test_sudoku.board)

    

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