from Tools import *
from importlib import import_module
from sys import modules
import subprocess


if __name__ == "__main__":
    print("  _____ _____ ____  __  __ ___ _   _    _    _ ")
    print(" |_   _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |")
    print("   | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |")
    print("   | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___")
    print("   |_| |_____|_| \\_\\_|  |_|___|_| \\_/_/   \\_\\_____|")
    print("   ____    _    __  __ _____     _   _ _   _ ____")
    print("  / ___|  / \\  |  \\/  | ____|   | | | | | | | __ )")
    print(" | |  _  / _ \\ | |\\/| |  _|     | |_| | | | |  _ \\")
    print(" | |_| |/ ___ \\| |  | | |___    |  _  | |_| | |_) |")
    print("  \\____/_/   \\_\\_|  |_|_____|   |_| |_|\\___/|____/\n")

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

        ext = choice(['y', 'n'], "WOULD YOU LIKE TO EXIT?(y/n)\n", "PLEASE ENTER A 'y' OR 'n':\n")

    switchScreen()
    print("GOOD-BYE!")
