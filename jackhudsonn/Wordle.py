from Tools import *


class Wordle:
    def __init__(self, word_length=5, max_guesses=6, validate_guesses=True):
        self.word_length = word_length
        self.max_guesses = max_guesses
        self.validate_guesses = validate_guesses

        self.check = []
        self.grid = []
        for i in range(max_guesses):
            temp_lst1 = []
            temp_lst2 = []
            for j in range(word_length):
                temp_lst1.append(' ')
                temp_lst2.append('*')
            self.check.append(temp_lst1)
            self.grid.append(temp_lst2)

        self.letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.guess_count = 0

        self.word_bank = open(f"jackhudsonn/WordleLibrary/{word_length}.txt").read().lower().split()
        self.word = random.choice(self.word_bank)

        self.guessed_words = []

    def printBoard(self) -> None:
        switchScreen()
        print("    JACKHUDSONN'S  WORDLE")
        for i in range(self.max_guesses):
            for j in range(self.word_length):
                print("    ", end='')
                if self.check[i][j] == ' ':
                    print(self.grid[i][j], end='')  # no highlight
                elif self.check[i][j] == '-':
                    print('\x1b[0;30;43m' + self.grid[i][j] + '\x1b[0m', end='')  # yellow
                elif self.check[i][j] == '✓':
                    print('\x1b[6;30;42m' + self.grid[i][j] + '\x1b[0m', end='')  # green
            print()

        print(f"\nLETTERS LEFT: ", end='')
        for i in range(len(self.letters_left)):
            if i % 7 == 0:
                print()
            print(self.letters_left[i], end=' ')
        print("\n")

    def loseContOrWin(self) -> int:
        if self.check[self.guess_count - 1] == ['✓', '✓', '✓', '✓', '✓']:
            return WIN
        elif self.guess_count == self.max_guesses:
            return LOSE
        return CONTINUE

    def guess(self) -> str:
        print(f"INPUT A {self.word_length}-LETTER WORD:")
        guess = input()
        if self.validate_guesses:
            while guess not in self.word_bank or guess in self.guessed_words:
                switchScreen()
                self.printBoard()
                print("PLEASE ENTER A VALID AND UN-GUESSED {self.word_length}-LETTER WORD:")
                guess = input()
        else:
            while len(guess) != self.word_length or guess in self.guessed_words:
                switchScreen()
                self.printBoard()
                print("PLEASE ENTER AN UN-GUESSED {self.word_length}-LETTER WORD:")
                guess = input()

        self.guessed_words.append(guess)
        return guess

    def updateLettersLeft(self, guess):
        for i in range(self.word_length):
            for j in range(len(self.letters_left)):
                if self.letters_left[j] == guess[i]:
                    self.letters_left.remove(self.letters_left[j])
                    break

    def inputNewGuess(self, guess):
        # guess + actual character hashmaps that will hold number of occurrences of particular character
        mp_guess = {}
        mp_actual = {}

        for i in range(self.word_length):
            if guess[i] in mp_guess.keys():
                mp_guess[guess[i]] = mp_guess.get(guess[i]) + 1
            else:
                mp_guess[guess[i]] = 1

            if self.word[i] in mp_actual.keys():
                mp_actual[self.word[i]] = mp_actual.get(self.word[i]) + 1
            else:
                mp_actual[self.word[i]] = 1

            self.grid[self.guess_count][i] = guess[i]

            # set all characters to a '-' (which makes char background yellow)
            # if contained anywhere in the guessed word
            if self.grid[self.guess_count][i] in self.word:
                self.check[self.guess_count][i] = '-'

            # set guessed characters that are correct in placement to '✓' (which makes char background green)
            if self.grid[self.guess_count][i] == self.word[i]:
                self.check[self.guess_count][i] = '✓'

        # take away over accounted for '-'s
        for i in range(self.word_length - 1, -1, -1):
            if self.check[self.guess_count][i] == '-':
                if mp_actual.get(guess[i]) < mp_guess.get(guess[i]):
                    self.check[self.guess_count][i] = ' '
                    mp_guess[guess[i]] = mp_guess.get(guess[i]) - 1

    def play(self):
        while self.loseContOrWin() == CONTINUE:
            switchScreen()
            self.printBoard()

            guess = self.guess()

            self.updateLettersLeft(guess)
            self.inputNewGuess(guess)

            self.guess_count += 1

        self.printBoard()
        if self.loseContOrWin() == LOSE:
            print(f"YOU LOSE! THE WORD WAS: {self.word}\n")
        elif self.loseContOrWin() == WIN:
            print(f"YOU WIN! THE WORD WAS: {self.word}\n")


Wordle(5, 6, True).play()
