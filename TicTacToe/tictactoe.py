from tictactoe_utils import *


player_1 = "a"
player_2 = "a"
while  player_1 not in "ox":
    player_1 = input("Make a valid choice (o or x): ").lower()
    if player_1 in "ox":
        if player_1 == 'o':
            player_2 = 'x'
        else:
            player_2 = 'o'

BOARD_SIZE = 3
board = create_board(BOARD_SIZE)
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

        line , column = select_position(BOARD_SIZE)

        if set_position(board,line-1,column-1,current_player) is None:
            print("This place is not free")
        else:
            board = set_position(board,line-1,column-1,current_player)
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
