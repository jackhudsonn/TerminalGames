from Tools import *


class Wordle:
    def __init__(self):
        self.check = [['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`'],
                      ['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`'],
                      ['`', '`', '`', '`', '`'], ['`', '`', '`', '`', '`']]
        self.grid = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
                     ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
                     ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]

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
            print(f"   {self.grid[i][0]}     {self.grid[i][1]}     {self.grid[i][2]}     "
                  f"{self.grid[i][3]}     {self.grid[i][4]}   ")
        print()

        print(f"LETTERS LEFT: ", end=' ')
        for i in range(len(self.letters_left)):
            print(self.letters_left[i], end=' ')
        print()
        switchScreen()

    def loseContOrWin(self) -> int:
        if self.check[self.guess_count - 1] == ['✓', '✓', '✓', '✓', '✓']:
            return WIN
        elif self.guess_count == 6:
            return LOSE
        return 0

    def guess(self) -> str:
        print("INPUT A FIVE-LETTER WORD:")
        word = input()
        while word not in self.word_bank:
            print("PLEASE ENTER A VALID FIVE-LETTER WORD:")
            word = input()

        return word

    def updateLettersLeft(self, guess):
        for i in range(5):
            for j in range(len(self.letters_left)):
                if self.letters_left[j] == guess[i]:
                    self.letters_left.remove(self.letters_left[j])
                    break

    def inputNewGuess(self, guess):
        mp_guess = {}
        mp_letters_correct = {}
        for i in range(5):
            mp_letters_correct[self.word[i]] = 0
            if guess[i] in mp_guess.keys():
                mp_guess[guess[i]] = mp_guess.get(guess[i]) + 1
            else:
                mp_guess[guess[i]] = 1

            self.grid[self.guess_count][i] = guess[i]

        for i in range(5):
            for j in range(5):
                if self.grid[self.guess_count][i] == self.word[j] and mp_guess.get(guess[i]) > 0:
                    self.check[self.guess_count][i] = '-'
                    mp_guess[guess[i]] = mp_guess.get(guess[i]) - 1
            if self.grid[self.guess_count][i] == self.word[i]:
                self.check[self.guess_count][i] = '✓'
                mp_letters_correct[self.word[i]] = mp_letters_correct.get(self.word[i]) + 1

        for i in range(5):
            if mp_letters_correct.get(guess[i]) is None:
                mp_letters_correct[guess[i]] = 0
            if mp_letters_correct.get(guess[i]) > 0 and self.check[self.guess_count][i] == '-':
                self.check[self.guess_count][i] = '*'
                mp_letters_correct[self.word[i]] = mp_letters_correct.get(self.word[i]) - 1

    def play(self):
        while self.loseContOrWin() == CONTINUE:
            self.printBoard()

            guess = self.guess()

            self.updateLettersLeft(guess)
            self.inputNewGuess(guess)

            self.guess_count += 1

        self.printBoard()
        if self.loseContOrWin() == LOSE:
            print(f"YOU LOSE! THE WORD WAS: {self.word}")
        elif self.loseContOrWin() == WIN:
            print(f"YOU WIN! THE WORD WAS: {self.word}")


Wordle().play()
