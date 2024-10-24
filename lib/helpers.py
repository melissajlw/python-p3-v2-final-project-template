import random

def is_valid(board, row, col, num):
    # Check if the number is not present in the same row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board [i][j] == num:
                return False
    return True
    
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(board):
    empty_cell = find_empty(board)
    # Board is solved
    if not empty_cell:
        return board
        
    row, col = empty_cell

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return board
            # Backtrack if current placement doesn't lead to a solution
            board[row][col] = 0
        # No valid number for current empty cell
    return False
    
def generate_solved():
    # Initialize an empty board
    board = [[0] * 9 for _ in range(9)]
    # Make sure board has a solution
    solve(board)
    # # Randomize the blank spaces 
    # empty_cells = random.sample([(i, j) for i in range (9) for j in range(9)], 40)
    # for cell in empty_cells:
    #     board[cell[0]][cell[1]] = 0
    return board

def generate_unsolved(difficulty, board):
    # Randomize the blank spaces 
    if difficulty == "easy":
        num = 1
    elif difficulty == "medium":
        num = 2
    elif difficulty == "hard":
        num = 3
    
    for _ in range(num):
        # Randomize the blank spaces n times based on difficulty
        empty_cells = random.sample([(i, j) for i in range (9) for j in range(9)], 40)
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 0
    return board

# slices string into chunks of size n
def slice_string(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

def string_to_board(board_string):
    # slices string into chunks of size 9
    board = slice_string(board_string, 9)

    # slices the string into individual characters
    res = list(map(lambda ele: list(ele), board))

    # changes the string to numeric
    for i in range(9):
        for j in range(9):
            res[i][j] = int(res[i][j])

    return res

def board_to_string(board):
    tmp_str = ""
    for i in range(9):
        for j in range(9):
            tmp_str = tmp_str + str(board[i][j])
    return tmp_str

# test_string = "123456789123456789123456789123456789123456789123456789123456789123456789123456789"
# board = string_to_board(test_string)
# print(board)
# test_string_2 = board_to_string(board)
# print(test_string_2)
# print(test_string.isnumeric())

# test_board = generate_solved()
# print(test_board)
# test_string = board_to_string(test_board)
# print(test_string)