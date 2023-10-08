from Tools import *


class Wordle:
    def __init__(self):
        self.check = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
        self.grid = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
                     ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
                     ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]

        self.letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.guess_count = 0

        self.word_bank = open("WordleLibrary.txt").read().split()
        self.word = random.choice(self.word_bank)
        self.word = "level"

    def printBoard(self) -> None:
        for i in range(6):
            print()
            for j in range(5):
                print("    ", end='')
                if self.check[i][j] == ' ':
                    print(self.grid[i][j], end='')
                elif self.check[i][j] == '-':
                    print('\x1b[0;30;43m' + self.grid[i][j] + '\x1b[0m', end='')
                elif self.check[i][j] == '✓':
                    print('\x1b[6;30;42m' + self.grid[i][j] + '\x1b[0m', end='')
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
        mp_actual = {}

        for i in range(5):
            if guess[i] in mp_guess.keys():
                mp_guess[guess[i]] = mp_guess.get(guess[i]) + 1
            else:
                mp_guess[guess[i]] = 1

            mp_letters_correct[self.word[i]] = 0

            if self.word[i] in mp_actual.keys():
                mp_actual[self.word[i]] = mp_actual.get(self.word[i]) + 1
            else:
                mp_actual[self.word[i]] = 1

            self.grid[self.guess_count][i] = guess[i]

        for i in range(5):
            for j in range(5):
                if self.grid[self.guess_count][i] == self.word[j]:
                    self.check[self.guess_count][i] = '-'
            if self.grid[self.guess_count][i] == self.word[i]:
                self.check[self.guess_count][i] = '✓'
                mp_letters_correct[self.word[i]] = mp_letters_correct.get(self.word[i]) + 1

        for i in range(5):
            if mp_letters_correct.get(guess[i]) is None:
                mp_letters_correct[guess[i]] = 0
            elif (mp_letters_correct.get(guess[i]) > 0 or False) and self.check[self.guess_count][i] == '-':
                self.check[self.guess_count][i] = ' '
                mp_letters_correct[self.word[i]] = mp_letters_correct.get(self.word[i]) - 1

        for i in range(4, -1, -1):
            if self.check[self.guess_count][i] == '-':
                if mp_actual.get(guess[i]) < mp_guess.get(guess[i]):
                    self.check[self.guess_count][i] = ' '
                    mp_guess[guess[i]] = mp_guess.get(guess[i]) - 1

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
