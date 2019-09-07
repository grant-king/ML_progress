from ttt_models import *

def test_board_winner_horizontal():
    board = Board()
    board.play('x' [0, 0])
    board.play('x' [1, 0])
    board.play('x' [2, 0])

    board.winner() = 'x'

def test_board_winner_vertical():
    pass

def test_board_winner_diagonal():
    pass
