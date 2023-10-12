import random
from getpass import getpass
import time
import os
import keyboard


# Functions
def choice(possibilities, text, invalid_text='') -> str:
    ret = input(text)

    while ret not in possibilities:
        ret = input(invalid_text)

    return ret


def switchScreen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def wait(seconds):
    time.sleep(seconds)


def hideText(prompt):
    getpass(prompt)


# Constants
WIN = 1
CONTINUE, TIE = 0, 0
LOSE = -1
