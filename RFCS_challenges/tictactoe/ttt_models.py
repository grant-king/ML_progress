import pygame
from pygame.locals import *
import random

class Board:
    def __init__(self):
        self.ROWS = 5 
        self.COLS = 5

        self.cells = [[Cell([row, column]) for row in range(self.ROWS)] for column in range(self.COLS)]
        #build list of unoccupied cells
        self.unoccupied_locations = []
        for cell_row in self.cells:
            for cell in cell_row:
                self.unoccupied_locations.append(cell.grid_idx)

        self.current_player = 'o'
        self.finished = False
        self.winner = None
        self.trial_board = False

        self.drawer = BoardDrawing(self)
        self.grader = BoardGrading(self)

    def update(self):
        self.drawer.draw()

    def copy(self):
        new_board = Board()
        for row_idx, cell_row in enumerate(self.cells):
            for col_idx, cell in enumerate(cell_row):
                if cell.occupied:
                    new_board.play(cell.symbol, [row_idx, col_idx])
        return new_board

    def play(self, symbol, grid_idx):
        if grid_idx in self.unoccupied_locations:
            self.unoccupied_locations.remove([grid_idx[0], grid_idx[1]])
            cell = self.cells[grid_idx[0]][grid_idx[1]]
            cell.occupy(symbol)
            self.grader.grade()
            self.toggle_player()

    def random_play(self, symbol):
        cell_location = random.choice(self.unoccupied_locations)
        self.play(symbol, cell_location)
        
            
    def toggle_player(self):
        if not self.finished:
            if self.current_player == 'x':
                self.current_player = 'o'
            else:
                self.current_player = 'x'

    def score(self, player_symbol):
        #return array of scores relative to player_symbol and board winner
        if self.finished:
            scores = [[0 for row in range(self.ROWS)] for column in range(self.COLS)]
            #return array of 0's if tie
            if self.winner == None:
                return scores
            else:
                #winner's occupied cells count for a point; loser's for negative point; empty no point.
                if self.winner == player_symbol:
                    multiplier = 1
                else:
                    multiplier = -1
                score = multiplier * 1
                #traverse cells, determine score for each if occupied
                #if player_symbol not winner, score is reversed
                for row_idx, cell_row in enumerate(self.cells):
                    for col_idx, cell in enumerate(cell_row):
                        if cell.occupied:
                            if cell.symbol == player_symbol:
                                scores[row_idx][col_idx] = score
                            else:
                                scores[row_idx][col_idx] = -score
                return scores


class BoardDrawing:
    def __init__(self, board):
        self.board = board

        self.cell_size = self.board.cells[0][0].size
        self.size = [self.cell_size[0] * self.board.COLS, self.cell_size[1] * self.board.ROWS]
        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect()
        
        self.generate_overlay()

    def draw(self):
        main_window = pygame.display.get_surface()

        #draw cells and contents
        for cell_row in self.board.cells:
            for cell in cell_row:
                cell.draw(self.surface)
        
        #add overlay
        self.surface.blit(self.border_overlay, self.rect)

        #draw composite on main display
        main_window.blit(self.surface, self.rect)

    def generate_overlay(self):
        overlay_color = [100, 100, 100]
        overlay_surface = pygame.Surface(self.size)
        overlay_surface.set_colorkey([0, 0, 0])
        line_width = 10

        vert_line_separation = self.size[0] // self.board.COLS
        horiz_line_separation = self.size[1] // self.board.ROWS
        
        for row in range(1, self.board.ROWS):
            start_pos = [0, row*horiz_line_separation]
            end_pos = [self.size[0], row*horiz_line_separation]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        for col in range(1, self.board.COLS):
            start_pos = [col*vert_line_separation, 0]
            end_pos = [col*vert_line_separation, self.size[1]]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        self.border_overlay = overlay_surface


class BoardGrading:
    def __init__(self, board):
        self.board = board

    def grade(self):
        #check for winning conditions
        counter = []

        #check horizontal matches
        for cell_row in self.board.cells:
            for cell in cell_row:
                if cell.occupied:                    
                    counter.append(cell.symbol)
            self.check_counter(counter, 'horizontal')
            counter.clear()
        counter.clear()
        
        #check vertical matches
        for column_idx in range(self.board.COLS):
            for cell_row in self.board.cells:
                if cell_row[column_idx].occupied:
                    counter.append(cell_row[column_idx].symbol)
            self.check_counter(counter, 'vertical')
            counter.clear()
        counter.clear()

        #check diagonal matches
        diagonal_cells = [[idx, idx] for idx in range(len(self.board.cells))]
        for cell_idx in diagonal_cells:
            if self.board.cells[cell_idx[0]][cell_idx[1]].occupied:
                counter.append(self.board.cells[cell_idx[0]][cell_idx[1]].symbol)
        self.check_counter(counter, 'diagonal')

        #check for full board:
        if self.board.winner == None and len(self.board.unoccupied_locations) == 0:
            self.board.finished = True
            if not self.board.trial_board:
                print('Draw')
    
    def check_counter(self, counter, direction_str):
        #check to determine if counter pattern contains enough in a row for win
        if counter == ['x' for repeat in range(self.board.COLS)] or counter == ['o' for repeat in range(self.board.COLS)]:
            self.board.winner = counter[0]
            self.board.finished = True
            if not self.board.trial_board:
                print(f'{self.board.winner} wins {direction_str}!')
                    

class Cell:
    def __init__(self, grid_idx):
        self.grid_idx = grid_idx
        self.size = [100, 100]
        self.coordinate_location = [grid_idx[0] * self.size[0], grid_idx[1] * self.size[1]]

        self.occupied = False
        self.symbol = '-'

        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.coordinate_location)

    def occupy(self, symbol):
        self.occupied = True
        self.symbol = symbol
        if symbol == 'x':
            self.surface.fill([250, 20, 100])
        else:
            self.surface.fill([50, 200, 100])

    def draw(self, grid_surface):
        grid_surface.blit(self.surface, self.rect)

    def __repr__(self):
        return f'{self.symbol}'


class MCMove:
    """
    Determine the next best move given the current board 
    """
    def __init__(self, board):
        self.starting_board = board.copy()
        self.player_perspective = self.starting_board.current_player
        self.board_score_total = [[0 for row in range(self.starting_board.ROWS)] for col in range(self.starting_board.COLS)]

    def add_board(self, score):
        for row_idx, score_row in enumerate(score):
            for col_idx, cell_score in enumerate(score_row):
                self.board_score_total[row_idx][col_idx] += cell_score

    def run_trials(self, num_trials=200):
        for trial in range(num_trials):
            #start individual games
            game_board = self.starting_board.copy()
            game_board.trial_board = True
            while not game_board.finished:
                game_board.random_play(game_board.current_player)
            self.add_board(game_board.score(self.player_perspective))

    def get_next_move(self):
        if len(self.starting_board.unoccupied_locations) > 0:
            #return 2d index of where best next move for
            self.run_trials()

            high_score = 0
            high_score_idx = random.choice(self.starting_board.unoccupied_locations)

            #get unoccupied cell with maximum value
            for row_idx, score_row in enumerate(self.board_score_total):
                for col_idx, score in enumerate(score_row):
                    if [row_idx, col_idx] in self.starting_board.unoccupied_locations:
                        if score > high_score:
                            high_score = score
                            high_score_idx[0] = row_idx
                            high_score_idx[1] = col_idx
            
            return high_score_idx
        return None
