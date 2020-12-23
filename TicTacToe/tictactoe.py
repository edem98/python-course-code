from tictactoe_utils import *


board = create_board()

player_1 = input("Make a choice (o or x): ").lower()
player_2 = ""
if player_1 in "ox":
    if player_1 == 'o':
        player_2 = 'x'
    else:
        player_2 = 'o'

current_player = player_1
game_state = is_winner(board,player_1,player_2)

while game_state is None :
    played = False
    while not played:
        print_board(board)
        if current_player == player_1:
            print("Player 1, is your turn to play")
        else:
            print("Player 2, is your turn to play")
        x = int(input("Enter your line: "))
        y = int(input("Enter your column: "))
        if set_position(board,x-1,y-1,current_player) is None:
            print("This place is not free")
        else:
            board = set_position(board,x-1,y-1,current_player)
            played = True

    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
    game_state = is_winner(board, player_1, player_2)

if game_state == "tie":
    print("Tie game")
elif game_state == player_1:
    print("Player 1 wins !!")
else:
    print("Player 2 wins !!")
