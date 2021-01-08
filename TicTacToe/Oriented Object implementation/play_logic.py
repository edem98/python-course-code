from tictactoe import *

# create players
player_1 = Player('serge', 'a')
player_2 = Player('edem', 'a')
# create board
board = Board(3)
board.create_board()
# setup game
game = TicTacToe(player_1,player_2,board)

while  player_1.sign not in "ox":
    player_1.sign = input("Make a valid choice (o or x): ").lower()
    if player_1.sign in "ox":
        if player_1.sign == 'o':
            player_2.sign = 'x'
        else:
            player_2.sign = 'o'

current_player = player_1
game_state = game.is_winner()


while game_state is None :
    played = False
    while not played:
        print(board)
        if current_player == player_1:
            print("{}, is your turn to play".format(player_1.name))
        else:
            print("{}, is your turn to play".format(player_2.name))

        line , column = game.select_position()

        if board.set_position(line-1,column-1,current_player) is None:
            print("This place is not free")
        else:
            board.set_position(line-1,column-1,current_player)
            played = True

    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1
    game_state = game.is_winner()

if game_state == "tie":
    print("Tie game")
elif game_state == player_1:
    print("{} wins !!".format(player_1))
else:
    print("{} wins !!".format(player_2))