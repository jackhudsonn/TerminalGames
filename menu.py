from Tools import *
from importlib import import_module
from sys import modules


def terminalGameHub() -> str:
    result = ""
    result += "  _____ _____ ____  __  __ ___ _   _    _    _ \n"
    result += " |_   _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |\n"
    result += "   | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |\n"
    result += "   | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___\n"
    result += "   |_| |_____|_| \\_\\_|  |_|___|_| \\_/_/   \\_\\_____|\n"
    result += "   ____    _    __  __ _____     _   _ _   _ ____\n"
    result += "  / ___|  / \\  |  \\/  | ____|   | | | | | | | __ )\n"
    result += " | |  _  / _ \\ | |\\/| |  _|     | |_| | | | |  _ \\\n"
    result += " | |_| |/ ___ \\| |  | | |___    |  _  | |_| | |_) |\n"
    result += "  \\____/_/   \\_\\_|  |_|_____|   |_| |_|\\___/|____/\n\n"
    return result


if __name__ == "__main__":
    cont = 'y'
    while cont == 'y':
        username = ''
        game = 'b'
        while game == 'b':
            switchScreen()
            username = choice(open("users.txt").read().split(),
                              terminalGameHub() + "ENTER A REGISTERED GITHUB USERNAME: ",
                              terminalGameHub() + "PLEASE RE-ENTER A VALID USERNAME\n"
                              "TO CHECK IF THIS IS A REGISTERED USERNAME, CHECK 'users.txt': ",
                              switch_on_fail=True)
            switchScreen()
            games = open(f"{username}/Games.txt").read().split()
            games.append('b')
            game = choice(games, f"GAME: ", "PLEASE RE-ENTER A VALID GAME OR PRESS 'b' TO GO BACK: ",
                          list_options=True,
                          pre_list_text=terminalGameHub()+f"ENTER THE GAME BY {username} "
                                                          f"THAT YOU WOULD LIKE TO PLAY OR PRESS 'b' TO GO BACK: ",
                          switch_on_fail=True)

        switchScreen()
        import_module(f"{username}.{game}")
        modules.pop(f"{username}.{game}")

        cont = choice(['y', 'n'], "\nWOULD YOU LIKE TO PLAY ANOTHER GAME?(y/n)\n", "PLEASE ENTER A 'y' OR 'n':\n")

    switchScreen()
    print("GOOD-BYE!")