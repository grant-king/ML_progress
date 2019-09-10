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

def test_board_score_x_winner():
    board = Board()

    board.play('x', [0, 0])
    board.play('x', [1, 1])
    board.play('x', [2, 2])

    board.play('o', [0, 1])
    board.play('o', [0, 2])
    
    board.grader.grade()

    expected_scores = [[1, -1, -1], [0, 1, 0], [0, 0, 1]]
    scores = board.score('x')

    assert scores == expected_scores

def test_mcmove_next_move():
    board = Board()

    board.play('x', [0, 0])
    board.play('x', [0, 1])

    board.play('o', [1, 1])
    board.play('o', [2, 2])

    board.current_player = 'x'

    mcmove = MCMove(board)
    next_location = mcmove.get_next_move()
    
    assert next_location == [0, 2]

def test_mcmove_tie():
    board = Board()

    board.play('o', [0, 1])
    board.play('x', [0, 0])
    board.play('o', [1, 0])
    board.play('x', [0, 2])
    board.play('o', [1, 1])
    board.play('x', [1, 2])
    board.play('o', [2, 0])
    board.play('x', [2, 1])
    board.play('o', [2, 2])

    board.grader.grade()

    next_location = MCMove(board).get_next_move()

    assert next_location == None

test_mcmove_tie()
