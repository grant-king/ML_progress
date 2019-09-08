import pygame
from pygame.locals import *
import random

class Board:
    def __init__(self):
        self.ROWS = 3 
        self.COLS = 3

        self.cells = [[Cell([row, column]) for row in range(self.ROWS)] for column in range(self.COLS)]
        #build list of unoccupied cells
        self.unoccupied_locations = []
        for cell_row in self.cells:
            for cell in cell_row:
                self.unoccupied_locations.append(cell.grid_idx)

        self.current_player = 'x'
        self.finished = False
        self.winner = None

        self.drawer = BoardDrawing(self)
        self.grader = BoardGrading(self)

    def update(self):
        self.grader.grade()
        self.drawer.draw()

    def score(self):
        #return array of scores relative to winner
        if self.finished:
            pass
    
    def copy(self):
        new_board = Board()
        for column_idx, cell_row in enumerate(self.cells):
            for row_idx, cell in enumerate(cell_row):
                if cell.occupied:
                    new_board.play(cell.symbol, [column_idx, row_idx])
        return new_board

    def play(self, symbol, grid_idx):
        cell = self.cells[grid_idx[0]][grid_idx[1]]
        cell.occupy(symbol)

    def random_play(self):
        if len(self.unoccupied_locations) > 0:
            cell_location = self.unoccupied_locations.pop(random.randrange(len(self.unoccupied_locations)))
            self.play(self.current_player, cell_location)
            self.toggle_player()

    def toggle_player(self):
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'


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
            print('Draw')
    
    def check_counter(self, counter, direction_str):
        #check to determine if counter pattern contains enough in a row for win
        if counter == ['x' for repeat in range(self.board.COLS)] or counter == ['o' for repeat in range(self.board.COLS)]:
            self.board.winner = counter[0]
            self.board.finished = True
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
        self.num_trials = 10
        self.starting_board = board.copy()
        self.run_trials()

    def run_trials(self):
        for trial in range(self.num_trials):
            #start individual games
            game_board = self.starting_board.copy()
            while game_board.unfinished:
                game_board.random_play()

            

