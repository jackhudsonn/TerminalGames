import random
from getpass import getpass
import time
import os
import keyboard


# Functions
def choice(possibilities, inquiry, invalid_text='', list_options=False, pre_list_text='', switch_on_fail=False) -> str:
    if list_options:
        print(pre_list_text)
        for possibility in possibilities:
            print(' ·' + possibility)

    ret = input(inquiry)

    while ret not in possibilities:
        if switch_on_fail:
            switchScreen()

        if list_options:
            print(pre_list_text)
            for possibility in possibilities:
                print(' ·' + possibility)

        ret = input(invalid_text)

    return ret


def switchScreen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def wait(seconds):
    time.sleep(seconds)


def hideText(prompt):
    getpass(prompt)


# Constants
WIN, RIGHT = 1, 1
CONTINUE, TIE, LEFT = 0, 0, 0
LOSE = -1

