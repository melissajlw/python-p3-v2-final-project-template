# lib/cli.py

from sudoku import Sudoku
import helpers
from globals import clear, space, any_key_to_continue, invalid_choice
from player import Player

class Cli():
    def start(self):
        clear()
        print("Let's play Sudoku!")
        self.main_menu()
    
    # MENU METHODS
    def restart_main_menu(self):
        any_key_to_continue()
        clear()
        self.main_menu()
    
    def restart_player_details(self, player):
        any_key_to_continue()
        clear()
        self.print_player_details(player)
        self.player_details_menu(player)
    
    def restart_difficulty_menu(self):
        any_key_to_continue()
        clear()
        self.difficulty_menu()
    
    def restart_sudoku_details(self, sudoku):
        any_key_to_continue()
        clear()
        self.sudoku_menu(sudoku)

    def main_menu(self):
        space()
        print("Enter 1 to see a list of previous players")
        print("Enter 2 to create a new player")
        print("Enter 3 to select a player")
        print("Enter 4 to see all Sudokus")
        print("Type exit to exit the program")
        self.main_menu_selection()
    
    def main_menu_selection(self):
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            self.list_players()
            self.restart_main_menu()
        elif user_input == "2":
            clear()
            name = str(input("Please enter your name: "))
            self.post_name_menu(name)
        elif user_input == "3":
            clear()
            self.select_player()
        elif user_input == "4":
            clear()
            self.list_sudokus()
            self.restart_main_menu()
        elif user_input == "exit":
            clear()
            print("Exiting program, goodbye!")
    
    def post_name_menu(self, name):
        space()
        Player.create(name)
        print("Player successfully created")
        print(f"Hello, {name}!")
    
    def difficulty_menu(self, player):
        clear()
        print("Select difficulty: ")
        print("Press 1 for easy")
        print("Press 2 for medium")
        print("Press 3 for hard")
        self.difficulty_selection(player)

    def difficulty_selection(self, player):
        space()
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            print("Easy Sudoku")
            print("----------")
            space()
            solved_board = helpers.generate_solved()
            board = helpers.generate_unsolved("easy", solved_board)
            sudoku = Sudoku.create(board=board, difficulty="easy")
            sudoku.link_player(player)
            clear()
            print("Created easy Sudoku successfully")
        elif user_input == "2":
            clear()
            print("Medium Sudoku")
            print("----------")
            space()
            solved_board = helpers.generate_solved()
            board = helpers.generate_unsolved("medium", solved_board)
            sudoku = Sudoku.create(board=board, difficulty="medium")
            sudoku.link_player(player)
            clear()
            print("Created medium Sudoku successfully")
        elif user_input == "3":
            clear()
            print("Hard Sudoku")
            print("----------")
            space()
            solved_board = helpers.generate_solved()
            board = helpers.generate_unsolved("hard", solved_board)
            sudoku = Sudoku.create(board=board, difficulty="hard")
            sudoku.link_player(player)
            clear()
            print("Created hard Sudoku successfully")
        else:
            clear()
            invalid_choice()
            self.restart_difficulty_menu()

    def list_players(self):
        print("Player List")
        print("----------")
        i = 1
        for player in Player.all():
            self.print_player(player, i)
            i = i + 1
    
    def print_player(self, player, list_number):
        print(f"{list_number}. {player.name}")

    def select_player(self):
        print("Select Player")
        print("----------")
        space()
        user_input = input("Enter number associated with player: ")
        try:
            index = int(user_input) - 1
            players = Player.all()
            if index in range(0, len(players)):
                player = players[index]
                clear()
                self.print_player_details(player)
                self.player_details_menu(player)
            else:
                clear()
                invalid_choice()
        except ValueError as error:
            clear()
            invalid_choice()
    
    def print_player_details(self, player):
        print(f"{player.name} Details")
        print("----------")
        space()
        print(f"Name: {player.name}")
        space()
        print("Sudokus:")
        self.print_player_sudokus(player)

    def player_details_menu(self, player):
        space()
        print(f"Type '1' to edit {player.name}")
        print(f"Type '2' to delete {player.name}")
        print("Type '3' to start a new Sudoku")
        print("Type '4' to continue a Sudoku")
        print("Enter '5' to see finished Sudokus")
        print("Enter '6' to select a Sudoku")
        print("Type 'main' to exit to main menu")
        space()
        self.player_details_menu_selection(player)
    
    def player_details_menu_selection(self, player):
        user_input = input("Enter Here: ")
        if user_input == "1":
            clear()
            self.edit_player(player)
            self.restart_player_details(player)
        elif user_input == "2":
            clear()
            if not self.delete_player(player):
                self.restart_player_details(player)
        elif user_input == "3":
            clear()
            self.difficulty_menu(player)
        elif user_input == "4":
            clear()
            print("Continue Sudoku")
        elif user_input == "5":
            clear()
            print("Finished Sudoku")
        elif user_input == "6":
            clear()
            self.print_player_sudokus(player)
            self.sudoku_selection_menu(player)
        elif user_input == "main":
            clear()
            print("Returning to the main menu")
        else:
            clear()
            invalid_choice()
            self.restart_player_details(player)
    
    def sudoku_selection_menu(self, player):
        print("Select Sudoku")
        print("----------")
        space()
        user_input = input("Enter number associated with Sudoku: ")
        try:
            index = int(user_input) - 1
            sudokus = player.sudokus()
            if index in range(0, len(sudokus)):
                sudoku = sudokus[index]
                clear()
                sudoku.display()
                self.sudoku_menu(sudoku)
            else:
                clear()
                invalid_choice()
        except ValueError as error:
            clear()
            invalid_choice()
    
    def sudoku_menu(self, sudoku):
        print("Type '1' to solve the sudoku")
        print("Type '2' to edit the sudoku")
        print("Type '3' to delete the sudoku")
        print("Type exit to exit to the main menu")
        self.sudoku_menu_choice(sudoku)

    def sudoku_menu_choice(self, sudoku):
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            sudoku.solve()
            sudoku.display()
        elif user_input == "2":
            clear()
            self.edit_sudoku(sudoku)
            self.restart_sudoku_details(sudoku)
        elif user_input == "3":
            clear()
            if not self.delete_sudoku(sudoku):
                self.restart_sudoku_details(sudoku)
        elif user_input == "exit":
            self.main_menu_selection()
        else:
            clear()
            invalid_choice()
    
    def edit_sudoku(self, sudoku):
        print(f"Edit Sudoku")
        sudoku.display()
        print("----------")
        space()
        self.edit_sudoku_selection(sudoku)
    
    def edit_sudoku_selection(self, sudoku):
        user_input = input("Do you want to update the Sudoku? (y/n): ")
        if user_input.lower() == "y":
            clear()
            print("Edit the string to update the Sudoku board")
            print(f"{sudoku.board}")
            board = input("Enter board string here: ")
            sudoku.board = board
            sudoku.save()

    def edit_player(self, player):
        print(f"Edit {player.name}")
        print("----------")
        space()
        self.edit_player_selection(player)
    
    def edit_player_selection(self, player):
        user_input = input("Do you want to update name? (y/n): ")
        if user_input.lower() == "y":
            clear()
            name = input("Enter name here: ")
            player.name = name
            player.save()
        
        clear()
        print(f"{player.name} has been updated")
    
    def delete_player(self, player):
        print(f"Delete {player.name}")
        print("----------")
        space()
        return self.delete_player_confirmation(player)
    
    def delete_player_confirmation(self, player):
        user_input = input("Type (y/n) to confirm deletion: ")
        if user_input.lower() == "y":
            for sudoku in player.sudokus():
                sudoku.unlink()
            player.delete()
            clear()
            print(f'deleting {player.name}')
            return True
        else:
            clear()
            print("Cancelled")
            return False
    
    def delete_sudoku(self, sudoku):
        print(f"Delete Sudoku?")
        sudoku.display()
        print("----------")
        space()
        return self.delete_sudoku_confirmation(sudoku)
    
    def delete_sudoku_confirmation(self, sudoku):
        user_input = input("Type (y/n) to confirm deletion: ")
        if user_input.lower() == "y":
            sudoku.delete()
            clear()
            print(f'deleting Sudoku')
            return True
        else:
            clear()
            print("Cancelled")
            return False
    
    def print_player_sudokus(self, player):
        i = 1
        for sudoku in player.sudokus():
            self.print_sudoku(sudoku, i)
            i = i + 1
    
    def print_sudoku(self, sudoku, list_number):
        print(f"{list_number}.")
        sudoku.display()

    def list_sudokus(self):
        print("Sudoku List")
        print("----------")
        i = 1
        for sudoku in Sudoku.all():
            self.print_sudoku(sudoku, i)
            i = i + 1
