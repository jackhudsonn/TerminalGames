from RockPaperScissors import RockPaperScissors
from TicTacToe import TicTacToe
from Wordle import Wordle
from BlackJack import BlackJack


def getGame() -> str:
    game_list = ['r', 't', 'w', 'b', 'x']

    print("PRESS 'r' TO PLAY ROCK PAPER SCISSORS")
    print("PRESS 't' TO PLAY TIC TAC TOE")
    print("PRESS 'w' TO PLAY WORDLE")
    print("PRESS 'b' TO PLAY BLACK JACK")
    print("PRESS 'x' TO EXIT")

    choice = input().lower()
    while choice not in game_list:
        print("PLEASE ENTER A VALID GAME!")
        choice = input().lower()

    return choice


def switchScreen() -> None:
    print(28 * '-')
    print()


if __name__ == "__main__":
    print("WELCOME TO JACK'S GAMES!!!")
    switchScreen()

    game = " "

    while game != 'x':
        game = getGame()

        if game == 'r':
            switchScreen()
            RockPaperScissors().play()
            switchScreen()
        elif game == 'w':
            switchScreen()
            Wordle().play()
            switchScreen()
        elif game == 'b':
            switchScreen()
            BlackJack().play()
            switchScreen()
        elif game == 't':
            switchScreen()
            TicTacToe().play()
            switchScreen()
        elif game != 'x':
            print("Please type a valid, single letter")

    switchScreen()
    print("GOOD-BYE!")
