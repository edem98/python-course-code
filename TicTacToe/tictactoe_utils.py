def create_board(n=3):
    return [ ["a" for y in range(n) ]  for x in range(n)]

def check_column(board,player,size=3):
    for i in range(size):
        count = 0
        j = 0
        while j < size:
            if board[i][j] == player:
                count += 1
            j += 1

        if count == size:
            return True
    return False

def check_line(board,player,size=3):
    for i in range(size):
        count = 0
        j = 0
        while j < size:
            if board[j][i] == player:
                count += 1
            j += 1

        if count == size:
            return True
    return False

def check_oblique(board,player,size=3):
    count = 0
    i = 0
    j = 0
    while i < size:
        if board[i][j] == player:
            count += 1
        j += 1
        i += 1

    if count == size:
        return True

    count = 0
    i = size - 1
    j = 0
    while i >= size :
        print(i,j)
        if board[i][j] == player :
            count += 1
        j += 1
        i -= 1

    if count == size :
        return True

    return False

def is_full(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "a":
                return False
    return True

def is_winner(board,player1,player2,):
    winner = None
    # check if player1 wins
    if check_column(board,player1,len(board)):
        winner = player1
        return winner
    if check_line(board,player1,len(board)):
        winner = player1
        return winner
    if check_oblique(board,player1,len(board)):
        winner = player1
        return winner
    # check if player2 wins
    if check_column(board,player2,len(board)):
        winner = player2
        return winner
    if check_line(board,player2,len(board)):
        winner = player2
        return winner
    if check_oblic(board,player2,len(board)):
        winner = player2
        return winner
    # check if board if full
    if is_full(board):
        winner = "tie"

    return winner

def set_position(board,x,y,player):
    if board[x][y] == "a":
        board[x][y] = player
        return board
    elif board[x][y] != "a":
        return board
    return None

def print_board(board):
    for line in board:
        print(line)
