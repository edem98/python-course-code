l = [
    ["x", "x", "o"],
    ["a", "a", "a"],
    ["o", "o", "x"],
]


def tic_tac_toe(l):
    player1 = "o"
    player2 = "x"
    winner = ""
    if l[0][0] == l[0][1] == l[0][2] == player1:
        winner = player1
    elif l[0][0] == l[0][1] == l[0][2] == player2:
        winner = player2
    if l[1][0] == l[1][1] == l[1][2] == player1:
        winner = player1
    elif l[1][0] == l[1][1] == l[1][2] == player2:
        winner = player2
    if l[2][0] == l[2][1] == l[2][2] == player1:
        winner = player1
    elif l[2][0] == l[2][1] == l[2][2] == player2:
        winner = player2
    if l[0][0] == l[1][0] == l[2][0] == player1:
        winner = player1
    elif l[0][0] == l[1][0] == l[2][0] == player2:
        winner = player2
    if l[0][1] == l[1][1] == l[2][1] == player1:
        winner = player1
    elif l[0][1] == l[1][1] == l[2][1] == player2:
        winner = player2
    if l[0][2] == l[1][2] == l[2][2] == player1:
        winner = player1
    elif l[0][2] == l[1][2] == l[2][2] == player2:
        winner = player2
    if l[0][0] == l[1][1] == l[2][2] == player1:
        winner = player1
    elif l[0][0] == l[1][1] == l[2][2] == player2:
        winner = player2
    if l[0][2] == l[1][1] == l[2][0] == player1:
        winner = player1
    elif l[0][2] == l[1][1] == l[2][0] == player2:
        winner = player2

    if winner == player1:
        return "Le joueur 1 a gagner"
    elif winner == player2:
        return "le joueur 2 a gagner"
    else:
        return "Aucun vainqeur"


print(tic_tac_toe(l))
