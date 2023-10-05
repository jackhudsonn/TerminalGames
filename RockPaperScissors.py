import random
import Constants as Const
from getpass import getpass


class RockPaperScissors:
    def __init__(self, is_multiplayer=False):
        self.choices = ['r', 'p', 's']
        self.is_multiplayer = is_multiplayer
        # consider adding a best of n feature

    def getPlayerMove(self) -> str:
        print("Rock, paper, or scissors?(r/p/s):")
        if self.is_multiplayer:
            player_move = getpass(prompt="Input is hidden: ")
        else:
            player_move = input()
        if player_move.lower() not in self.choices:
            print("Please enter r, p, or s:")
            if self.is_multiplayer:
                player_move = getpass(prompt="Input is hidden: ")
            else:
                player_move = input()

        return player_move

    def getComputerMove(self) -> str:
        return self.choices[random.randint(0, 2)]

    def checkWinner(self, p1_move, p2_move) -> int:
        if p1_move == p2_move:
            return Const.CONTINUE
        elif (p2_move == 'r' and p1_move == 's') or (p2_move == 'p' and p1_move == 'r')\
                or (p2_move == 's' and p1_move == 'p'):
            return Const.LOSE
        else:
            return Const.WIN

    def play(self):
        if self.is_multiplayer:
            p1_name = "Player(1)"
            p2_name = "Player(2)"

            player_1_move = self.getPlayerMove()
            player_2_move = self.getPlayerMove()
        else:
            p1_name = "Player"
            p2_name = "Computer"

            player_1_move = self.getPlayerMove()
            player_2_move = self.getComputerMove()

        winner = self.checkWinner(player_1_move, player_2_move)
        letter_word = {'r': "rock", 'p': "paper", 's': "scissors"}

        if winner == Const.CONTINUE:
            print(f"Both {p1_name} and {p2_name} chose {player_1_move}...")
            print("TIE!")
        elif winner == Const.WIN:
            print(f"{letter_word.get(player_1_move)} beats {letter_word.get(player_2_move)}...")
            print(f"{p1_name} Wins!")
        else:
            print(f"{letter_word.get(player_2_move)} beats {letter_word.get(player_1_move)}...")
            print(f"{p2_name} Wins!")


if __name__ == "__main__":
    answer = "y"
    while answer.lower() == 'y':
        RockPaperScissors(is_multiplayer=True).play()
        answer = input("Would you like to play again? (y/n)\n")
