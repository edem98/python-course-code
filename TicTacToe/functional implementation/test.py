import  unittest
from tictactoe_utils import *

class TicTacToeTest(unittest.TestCase):

    def test_create_board(self,):
        self.assertEqual(create_board(), [["a","a","a"],["a","a","a"],["a","a","a"]])

    def test_create_board_of_size(self,):
        self.assertEqual(create_board(5),[["a","a","a","a","a"],["a","a","a","a","a"],["a","a","a","a","a"],["a","a","a","a","a"],["a","a","a","a","a"]])

    def test_check_column(self):
        board = create_board()
        player = "x"
        self.assertEqual(check_column(board,player), False)

    def test_check_column_player_wins(self):
        player = "x"
        board = [["x","a","a"],
                 ["x","a","a"],
                 ["x","a","a"]]
        self.assertEqual(check_column(board, player), True)

    def test_check_line(self):
        player = "x"
        board = [["x", "a", "a"],
                 ["x", "a", "a"],
                 ["x", "a", "a"]]
        self.assertEqual(check_line(board, player), False)

    def test_check_line_player_wins(self):
        player = "x"
        board = [["x", "x", "x"],
                 ["o", "o", "x"],
                 ["x", "o", "o"]]
        self.assertEqual(check_line(board, player), True)

    def test_check_oblique(self):
        player = "x"
        board = [["x", "a", "a"],
                 ["x", "a", "a"],
                 ["x", "a", "a"]]
        self.assertEqual(check_oblique(board, player), False)

    def test_check_oblique_player_wins(self):
        player = "x"
        board = [["x", "a", "a"],
                 ["o", "x", "o"],
                 ["x", "a", "x"]]
        self.assertEqual(check_oblique(board, player), True)

    def test_board_is_not_full(self):
        board = [["x", "a", "a"],
                 ["o", "x", "o"],
                 ["x", "a", "x"]]
        self.assertEqual(is_full(board), False)

    def test_board_is_full(self):
        board = [["x", "o", "x"],
                 ["o", "x", "o"],
                 ["x", "o", "x"]]
        self.assertEqual(is_full(board), True)

    def test_we_got_a_winner(self):
        player1 = "x"
        player2 = "o"
        board = [["x", "o", "x"],
                 ["o", "x", "o"],
                 ["x", "o", "x"]]
        self.assertEqual(is_winner(board,player1,player2), player1)

    def test_is_a_tie_game(self):
        player1 = "x"
        player2 = "o"
        board = [["x", "o", "x"],
                 ["o", "x", "o"],
                 ["x", "x", "o"]]
        self.assertEqual(is_winner(board,player1,player2), "tie")

    def test_game_not_tie(self):
        player1 = "x"
        player2 = "o"
        board = [["x", "o", "a"],
                 ["o", "x", "o"],
                 ["x", "x", "o"]]
        self.assertIsNone(is_winner(board, player1, player2))

    def test_set_position(self):
        player = "x"
        board = [["a", "o", "a"],
                 ["o", "x", "o"],
                 ["x", "x", "o"]]
        end_board = [["x", "o", "a"],
                     ["o", "x", "o"],
                     ["x", "x", "o"]]
        self.assertEqual(set_position(board,0,0,player),end_board)

    def test_set_position_to_taken_place(self):
        player = "o"
        board = [["x", "o", "a"],
                 ["o", "x", "o"],
                 ["x", "x", "o"]]
        end_board = [["x", "o", "a"],
                     ["o", "x", "o"],
                     ["x", "x", "o"]]
        self.assertEqual(set_position(board,0,0,player),end_board)

    def test_select_position(self):
        size = 3
        self.assertIn(select_position(size), [(1,2),(2,1),(2,2),(1,1),(1,3),(3,1),(3,3),(3,2),(2,3)])


if __name__ == '__main__':
    unittest.main()