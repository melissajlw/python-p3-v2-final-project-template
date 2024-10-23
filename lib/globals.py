import os

def clear():
    os.system("clear")

def space():
    print("")

def any_key_to_continue():
    space()
    input("Press any key to continue...")

def invalid_choice():
    space()
    print("Invalid Choice")