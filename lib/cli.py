# lib/cli.py

from sudoku import Sudoku
from globals import clear, space, any_key_to_continue, invalid_choice

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

    def main_menu(self):
        space()
        name = str(input("Please enter your name: "))
        self.post_name_menu(name)
    
    def post_name_menu(self, name):
        space()
        print(f"Hello, {name}!")
        print("Press 1 to start a new Sudoku")
        print("Press 2 to continue a Sudoku")
        print("Press 3 to see finished Sudoku")
        print("Type exit to exit the program")
        space()
        self.post_name_selection()
    
    def post_name_selection(self):
        space()
        user_input = input("Enter here: ")
        if user_input == 1:
            clear()
            print("New Sudoku")
        elif user_input == 2:
            clear()
            print("Continue Sudoku")
        elif user_input == 3:
            clear()
            print("Finished Sudoku")
        elif user_input == "exit":
            clear()
            print("Exiting program, goodbye!")

    

    
    def main():
        pass


if __name__ == "__main__":
    main()
