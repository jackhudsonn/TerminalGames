class TicTacToe:
    def __init__(self):
        blank = ' '
        self.board = [[blank, blank, blank],
                      [blank, blank, blank],
                      [blank, blank, blank]]

    def displayCurrentState(self) -> None:
        print("    1     2     3")
        print(f"1   {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  ")
        print("  +----+-----+----+")
        print(f"2   {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  ")
        print("  +----+-----+----+")
        print(f"3   {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  ")

    def turn(self, x_turn) -> None:
        valid = False
        row = -1
        col = -1

        while not valid:
            try:
                row = int(input("INPUT DESIRED ROW: ")) - 1
                assert 0 <= row <= 2

                col = int(input("INPUT DESIRED COLUMN: ")) - 1
                assert 0 <= col <= 2

                assert self.board[row][col] == ' '

                print()
                valid = True
            except AssertionError:
                print("\nBOTH ROW AND COLUMN MUST BE BETWEEN 1 AND 3 (INCLUSIVE), AND THE LOCATION MUST BE EMPTY")
            except ValueError:
                print("\nBOTH ROW AND COLUMN MUST BE INTEGERS")

        if x_turn:
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'O'

    def winCheck(self) -> str:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] or \
               self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[i][0]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
           self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[1][1]

        return ' '

    def play(self) -> None:
        count = 0
        while True:
            x_turn = True
            self.displayCurrentState()
            print("\nX TURN:")
            self.turn(x_turn)
            winner = self.winCheck()
            count += 1
            if winner != ' ':
                self.displayCurrentState()
                print(f"\nTHREE IN A ROW! {winner} WINS!")
                return
            elif count == 9:
                self.displayCurrentState()
                print(f"\nNEITHER PLAYER HAS THREE IN A ROW! TIE!")
                return

            x_turn = False
            self.displayCurrentState()
            print("\nO TURN:")
            self.turn(x_turn)
            winner = self.winCheck()
            count += 1
            if winner != ' ':
                self.displayCurrentState()
                print(f"\nTHREE IN A ROW! {winner} WINS!")
                return


if __name__ == "__main__":
    answer = "y"
    while answer.lower() == 'y':
        TicTacToe().play()
        answer = input("Would you like to play again? (y/n)")
