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

        self.letters_left = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.guess_count = 0

        self.word_bank = open(f"jackhudsonn/WordleLibrary/{word_length}.txt").read().upper().split()
        if word_length == 5:
            self.word_bank = open("jackhudsonn/WordleLibrary/RealWordleWords.txt").read().upper().split()
        self.word = random.choice(self.word_bank)
        self.word_bank = open(f"jackhudsonn/WordleLibrary/{word_length}.txt").read().upper().split()

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
            print(self.letters_left[i].upper(), end=' ')
        print("\n")

    def loseContOrWin(self) -> int:
        if self.check[self.guess_count - 1] == ['✓', '✓', '✓', '✓', '✓']:
            return WIN
        elif self.guess_count == self.max_guesses:
            return LOSE
        return CONTINUE

    def guess(self) -> str:
        print(f"INPUT A {self.word_length}-LETTER WORD:")
        guess = input().upper()
        if self.validate_guesses:
            while guess not in self.word_bank or guess in self.guessed_words:
                switchScreen()
                self.printBoard()
                print(f"PLEASE ENTER A VALID AND UN-GUESSED {self.word_length}-LETTER WORD:")
                guess = input().upper()
        else:
            while len(guess) != self.word_length or guess in self.guessed_words:
                switchScreen()
                self.printBoard()
                print(f"PLEASE ENTER AN UN-GUESSED {self.word_length}-LETTER WORD:")
                guess = input().upper()

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

guess_count = int(choice(['2', '3', '4', '5', '6', '7', '8', '9', '10'], "JACKHUDSONN'S  WORDLE\nHOW MANY GUESSES WOULD YOU LIKE?\nTYPE A NUMBER BETWEEN 2 and 10 (6 IF YOU WANT STANDARD WORDLE): ",
                            "JACKHUDSONN'S  WORDLE\nPLEASE TYPE A NUMBER, OF GUESSES, BETWEEN 2 and 10: ", switch_on_fail=True))
switchScreen()

letter_count = int(choice(['2', '3', '4', '5', '6', '7'], "JACKHUDSONN'S  WORDLE\nWHAT WORD LENGTH, IN LETTERS, WOULD YOU LIKE?\nTYPE A NUMBER BETWEEN 2 and 7 (5 IF YOU WANT STANDARD WORDLE): ",
                        "JACKHUDSONN'S  WORDLE\nPLEASE TYPE THE NUMBER OF LETTERS YOU WOULD LIKE BETWEEN 2 and 7: ", switch_on_fail=True))
switchScreen()

validate_word = choice(['y', 'n'], "WOULD YOU LIKE YOUR GUESSES TO BE VALIDTED/CHECKED IN THE WORDBANK?\nTYPE 'y' or 'n' ('y' IF YOU WANT STANDARD WORDLE): ",
                        "JACKHUDSONN'S  WORDLE\nPLEASE TYPE 'y' or 'n': ", switch_on_fail=True)
switchScreen()

Wordle(letter_count, guess_count, validate_word == 'y').play()

