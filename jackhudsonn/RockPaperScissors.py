from Tools import *


class RockPaperScissors:
    def __init__(self, is_multiplayer, best_of):
        self.choices = ['r', 'p', 's']
        self.is_multiplayer = is_multiplayer
        self.best_of = best_of

    def getPlayerMove(self) -> str:
        print("ROCK, PAPER, OR SCISSORS?(r/p/s):")
        if self.is_multiplayer:
            player_move = hideText(prompt="INPUT IS HIDDEN: ")
        else:
            player_move = input()
            
        if player_move.lower() not in self.choices:
            print("Please enter r, p, or s:")
            if self.is_multiplayer:
                player_move = hideText(prompt="INPUT IS HIDDEN: ")
            else:
                player_move = input()

        return player_move

    def getComputerMove(self) -> str:
        return self.choices[random.randint(0, 2)]

    def checkWinner(self, p1_move, p2_move) -> int:
        if p1_move == p2_move:
            return CONTINUE
        elif (p2_move == 'r' and p1_move == 's') or (p2_move == 'p' and p1_move == 'r') \
                or (p2_move == 's' and p1_move == 'p'):
            return LOSE
        else:
            return WIN

    def play(self):
        while self.best_of > 0:
            if self.is_multiplayer:
                p1_name = "PLAYER(1)"
                p2_name = "PLAYER(2)"

                player_1_move = self.getPlayerMove()
                player_2_move = self.getPlayerMove()
            else:
                p1_name = "PLAYER"
                p2_name = "COMPUTER"

                player_1_move = self.getPlayerMove()
                player_2_move = self.getComputerMove()

            winner = self.checkWinner(player_1_move, player_2_move)
            letter_word = {'r': "ROCK", 'p': "PAPER", 's': "SCISSORS"}

            if winner == CONTINUE:
                print(f"BOTH {p1_name} AND {p2_name} CHOSE {letter_word.get(player_1_move).upper()}...")
                print("TIE!")
            elif winner == WIN:
                print(f"{letter_word.get(player_1_move).upper()} BEATS {letter_word.get(player_2_move).upper()}...")
                print(f"{p1_name} WINS!")
            else:
                print(f"{letter_word.get(player_2_move).upper()} BEATS {letter_word.get(player_1_move).upper()}...")
                print(f"{p2_name} WINS!")

            self.best_of -= 1


RockPaperScissors(choice(['s', 'm'], "SINGLE PLAYER OR MULTIPLAYER? (s/m)", "PLEASE ENTER AN 's' OR AN 'm'") == 'm',
                  int(choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'], "BEST OF (ENTER A NUMBER 1-9): ",
                             "PLEASE ENTER A NUMBER 1-9"))).play()
