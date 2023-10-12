from Tools import *


class Wordle:
    def __init__(self):
        self.check = []
        self.grid = []
        for i in range(6):
            temp_lst1 = []
            temp_lst2 = []
            for j in range(5):
                temp_lst1.append(' ')
                temp_lst2.append('*')
            self.check.append(temp_lst1)
            self.grid.append(temp_lst2)

        self.letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.guess_count = 0

        self.word_bank = open("WordleLibrary.txt").read().split()
        self.word = random.choice(self.word_bank)

    def printBoard(self) -> None:
        switchScreen()
        # print(" ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____")
        # print("||j |||a |||c |||k |||h |||u |||d |||s |||o |||n |||' |||s |||       |||W |||o |||r |||d |||l |||e ||")
        # print("||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__||")
        # print("|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/_"
        #       "_\\|/__\\|/__\\|/_______\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|")
        print("    jackhudsonn's  Wordle")
        for i in range(6):
            for j in range(5):
                print("    ", end='')
                if self.check[i][j] == ' ':
                    print(self.grid[i][j], end='')
                elif self.check[i][j] == '-':
                    print('\x1b[0;30;43m' + self.grid[i][j] + '\x1b[0m', end='')  # yellow
                elif self.check[i][j] == '✓':
                    print('\x1b[6;30;42m' + self.grid[i][j] + '\x1b[0m', end='')  # green
            print()

        print(f"\nLETTERS LEFT: ")
        for i in range(len(self.letters_left)):
            print(self.letters_left[i], end=' ')
        print("\n")

    def loseContOrWin(self) -> int:
        if self.check[self.guess_count - 1] == ['✓', '✓', '✓', '✓', '✓']:
            return WIN
        elif self.guess_count == 6:
            return LOSE
        return CONTINUE

    def guess(self) -> str:
        print("INPUT A FIVE-LETTER WORD:")
        word = input()
        while word not in self.word_bank:
            switchScreen()
            self.printBoard()
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
        # guess + actual character hashmaps that will hold number of occurrences of particular character
        mp_guess = {}
        mp_actual = {}

        for i in range(5):
            if guess[i] in mp_guess.keys():
                mp_guess[guess[i]] = mp_guess.get(guess[i]) + 1
            else:
                mp_guess[guess[i]] = 1

            if self.word[i] in mp_actual.keys():
                mp_actual[self.word[i]] = mp_actual.get(self.word[i]) + 1
            else:
                mp_actual[self.word[i]] = 1

            self.grid[self.guess_count][i] = guess[i]

            for j in range(5):
                # set all characters to a '-' (which makes char background yellow)
                # if contained anywhere in the guessed word
                if self.grid[self.guess_count][i] == self.word[j]:
                    self.check[self.guess_count][i] = '-'

            # set guessed characters that are correct in placement to '✓' (which makes char background green)
            if self.grid[self.guess_count][i] == self.word[i]:
                self.check[self.guess_count][i] = '✓'

        # take away over accounted for '-'s
        for i in range(4, -1, -1):
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


Wordle().play()
