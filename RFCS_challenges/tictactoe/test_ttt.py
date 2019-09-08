from ttt_models import *

def test_board_winner_horizontal():
    board = Board()
    board.play('x', [0, 0])
    board.play('x', [0, 1])
    board.play('x', [0, 2])

    board.grader.grade()
    assert board.winner == 'x'

def test_board_winner_vertical():
    board = Board()
    board.play('x', [0, 0])
    board.play('x', [1, 0])
    board.play('x', [2, 0])
    
    board.grader.grade()
    assert board.winner == 'x'

def test_board_winner_diagonal():
    board = Board()
    board.play('x', [0, 0])
    board.play('x', [1, 1])
    board.play('x', [2, 2])
    
    board.grader.grade()
    assert board.winner == 'x'

def test_board_no_winner():
    board = Board()
    board.grader.grade()
    assert board.winner == None

