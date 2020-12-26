class Player:

    def __init__(self,name,sign):
        self.name = name
        self.sign = sign

    def __str__(self):
        return self.name


class Board:

    def __init__(self,size=3):
        self.size = size
        self.board = []

    def create_board(self):
        self.board = [["a" for y in range(self.size)] for x in range(self.size)]
        return self.board

    def check_column(self, player) :
        for i in range(self.size) :
            count = 0
            j = 0
            while j < self.size :
                if self.board[j][i] == player.sign :
                    count += 1
                j += 1
            print(count)
            if count == self.size :
                return True
        return False

    def check_line(self, player) :
        for i in range(self.size) :
            count = 0
            j = 0
            while j < self.size :
                if self.board[i][j] == player.sign :
                    count += 1
                j += 1
            if count == self.size :
                return True
        return False

    def check_oblique(self, player) :
        count = 0
        i = 0
        j = 0
        while i < self.size :
            if self.board[i][j] == player.sign :
                count += 1
            j += 1
            i += 1

        if count == self.size :
            return True

        count = 0
        i = self.size - 1
        j = 0
        while i >= self.size :
            if self.board[i][j] == player.sign :
                count += 1
            j += 1
            i -= 1

        if count == self.size :
            return True

        return False

    def is_full(self) :
        for i in range(len(self.board)) :
            for j in range(len(self.board)) :
                if self.board[i][j] == "a" :
                    return False
        return True

    def set_position(self, x, y, player) :
        if self.board[x][y] == "a" :
            self.board[x][y] = player.sign
            return self
        elif self.board[x][y] != "a" :
            return self
        return None

    def __str__(self):
        output = ''
        for line in self.board:
            output += '|'.join(line) + "\n"
        return output


class TicTacToe:

    def __init__(self,player1,player2,board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def select_position(self) :
        line = self.board.size + 1
        column = self.board.size + 1
        while line > self.board.size or column > self.board.size :
            try :
                line = int(input("Enter your line (a valid line): "))
                column = int(input("Enter your column (a valid column): "))
            except ValueError :
                print("Your input are not all integers,lower or equal to the size of the board ({}) ".format(self.board.size))

        return line, column

    def is_winner(self) :
        winner = None
        # check if player1 wins
        if self.board.check_column(self.player1) :
            winner = self.player1
            return winner
        if self.board.check_line(self.player1) :
            winner = self.player1
            return winner
        if self.board.check_oblique(self.player1) :
            winner = self.player1
            return winner
        # check if player2 wins
        if self.board.check_column(self.player2) :
            winner = self.player2
            return winner
        if self.board.check_line(self.player2) :
            winner = self.player2
            return winner
        if self.board.check_oblique(self.player2) :
            winner = self.player2
            return winner
        # check if board if full
        if self.board.is_full() :
            winner = "tie"

        return winner