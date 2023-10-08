from Tools import *
from importlib import import_module
from sys import modules
import subprocess


if __name__ == "__main__":
    print("WELCOME TO THE TERMINAL GAME HUB!!!")
    switchScreen()

    ext = 'n'
    while ext == 'n':
        username = choice(open("users.txt").read().split(),
                          "ENTER A REGISTERED GITHUB USERNAME:\n",
                          "PLEASE RE-ENTER A VALID USERNAME\n"
                          "TO CHECK IF THIS IS A REGISTERED USERNAME, CHECK 'users.txt':\n")
        game = choice(open(f"{username}_games.txt").read().split(),
                      f"ENTER THE GAME BY {username} THAT YOU WOULD LIKE TO PLAY:\n",
                      "PLEASE RE-ENTER A VALID GAME\n"
                      f"TO CHECK IF THIS IS A REGISTERED GAME, CHECK '{username}_games.txt':\n")
        file_name = username + '_' + game

        switchScreen()

        import_module(file_name)
        modules.pop(file_name)

        switchScreen()

        ext = choice(['y', 'n'], "WOULD YOU LIKE TO EXIT?(y/n)\n", "PLEASE ENTER A 'y' OR 'n':\n")

    switchScreen()
    print("GOOD-BYE!")
