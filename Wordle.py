import random
import Constants as Const


class Wordle:
    def __init__(self):
        empty = ' '
        self.check = [[empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty]]
        self.grid = [[empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty],
                     [empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty],
                     [empty, empty, empty, empty, empty], [empty, empty, empty, empty, empty]]

        self.letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.guess_count = 0

        self.word_bank = open("WordleLibrary.txt").read().split()
        self.word = random.choice(self.word_bank)

    def printBoard(self) -> None:
        for i in range(6):
            print()
            print(f"   {self.check[i][0]}     {self.check[i][1]}     {self.check[i][2]}     "
                  f"{self.check[i][3]}     {self.check[i][4]}")
            print("+-----+-----+-----+-----+-----+")
            print(f"|  {self.grid[i][0]}  |  {self.grid[i][1]}  |  {self.grid[i][2]}  |  "
                  f"{self.grid[i][3]}  |  {self.grid[i][4]}  |")
            print("+-----+-----+-----+-----+-----+")
        print()

        print(f"Letters Left: ", end=' ')
        for i in range(len(self.letters_left)):
            print(self.letters_left[i], end=' ')
        print("")
        print('-' * 28)
        print("")

    def loseContOrWin(self) -> int:
        if self.check[self.guess_count - 1] == ['✓', '✓', '✓', '✓', '✓']:
            return Const.WIN
        elif self.guess_count == 6:
            return Const.LOSE
        return 0

    def guess(self) -> str:
        print("Input your five letter word:")
        word = input()
        while word not in self.word_bank:
            print("Please enter a valid five letter word:")
            word = input()

        return word

    def updateLettersLeft(self, guess):
        for i in range(5):
            for j in range(len(self.letters_left)):
                if self.letters_left[j] == guess[i]:
                    self.letters_left.remove(self.letters_left[j])
                    break

    def inputNewGuess(self, guess):
        for i in range(5):
            self.grid[self.guess_count][i] = guess[i]

        for i in range(5):
            for j in range(5):
                if self.grid[self.guess_count][i] == self.word[j]:
                    self.check[self.guess_count][i] = '-'
            if self.grid[self.guess_count][i] == self.word[i]:
                self.check[self.guess_count][i] = '✓'

    def play(self):
        while self.loseContOrWin() == Const.CONTINUE:
            self.printBoard()

            guess = self.guess()

            self.updateLettersLeft(guess)
            self.inputNewGuess(guess)

            self.guess_count += 1

        self.printBoard()
        if self.loseContOrWin() == Const.LOSE:
            print(f"YOU LOSE! THE WORD WAS: {self.word}")
        elif self.loseContOrWin() == Const.WIN:
            print(f"YOU WIN! THE WORD WAS: {self.word}")


if __name__ == "__main__":
    answer = "y"
    while answer.lower() == 'y':
        Wordle().play()
        answer = input("Would you like to play again? (y/n)\n")
