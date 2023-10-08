import random
from getpass import getpass
import time
import os


# Functions
def choice(possibilities, text, invalid_text='') -> str:
    ret = input(text)

    while ret not in possibilities:
        ret = input(invalid_text)

    return ret


def switchScreen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


# Constants
WIN = 1
CONTINUE, TIE = 0, 0
LOSE = -1

