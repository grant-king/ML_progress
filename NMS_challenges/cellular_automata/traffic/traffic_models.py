import pygame
from pygame.locals import *
import random

class Cell(pygame.sprite.Sprite):
    def __init__(self, square_size, column_idx, row_idx, living=False):
        super(Cell, self).__init__()
        
        startx = square_size * column_idx
        starty = square_size * row_idx

        self.START_LOC = [startx, starty]

        self.column_idx = column_idx 
        self.row_idx = row_idx

        blue = random.randint(50, 110)
        self.color = [255-blue, 80, blue]
        self.size = [square_size, square_size]
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        
        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.START_LOC)

        self.alive = living

    def update(self):
        self.update_states()
        self.draw()

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_states(self):
        if self.alive:
            self.surface.fill(self.color)
        else:
            self.surface.fill([0, 0, 0])

class Stoplight(Cell):
    def __init__(self, square_size, column_idx, row_idx):
        super().__init__(square_size, column_idx, row_idx)

        self.SWITCH_FRAMES = random.randint(15, 40) # frames before switch
        self.switch_ticks = 0
        self.signal_state = 'red'
    
    def toggle_signal(self):
        if self.signal_state == 'red':
            self.signal_state = 'green'
        else:
            self.signal_state = 'red'

    def update(self):
        self.update_states()
        self.draw()
    
    def update_states(self):
        self.switch_ticks += 1
        if self.switch_ticks > self.SWITCH_FRAMES:
            self.switch_ticks = 0
            self.toggle_signal()

        if self.signal_state == 'red':
            self.surface.fill([240, 10, 5])
        elif self.signal_state == 'green':
            self.surface.fill([5, 240, 10])
        else:
            self.surface.fill([240, 240, 60])

class Lane:
    def __init__(self, cell_size, row_idx, num_active, direction=1):
        self.row_idx = row_idx
        self.direction = direction
        self.num_active = num_active
        
        self.SCREEN_SIZE = pygame.display.get_surface().get_size()
        self.CELL_SIZE = cell_size

        self.total_columns = self.SCREEN_SIZE[0] // self.CELL_SIZE
        self.total_rows = self.SCREEN_SIZE[1] // self.CELL_SIZE
        
        self.cells = []
        self.build_cells()

    def build_cells(self):
        #initialize full row of dead cells
        for col_idx in range(self.total_columns):
            self.cells.append(Cell(self.CELL_SIZE, col_idx, self.row_idx))

        #add stoplight
        light_idx = random.randrange(self.total_columns)
        self.stoplight = Stoplight(self.CELL_SIZE, light_idx, self.row_idx)

        for cell_idx in range(self.num_active):
            self.cells[cell_idx].alive = True

    def redlight(self, idx):
        if self.stoplight.signal_state == 'red':
            return idx == self.stoplight.column_idx
        else:
            return False

    def update(self):
        current_states = list([cell.alive for cell in self.cells])
        kill_cells, activate_cells = [], []

        for idx, cell in enumerate(self.cells):
            #wrap display
            if idx < len(self.cells) - 1:
                forward_neighbor = idx + 1
            else:
                forward_neighbor = 0

            #move forward only if space available,  not red light
            if current_states[idx] and not self.redlight(idx) and not current_states[forward_neighbor]:
                kill_cells.append(idx)
                activate_cells.append(forward_neighbor)
        
        for cell_idx in kill_cells:
            self.cells[cell_idx].alive = False

        for cell_idx in activate_cells:
            self.cells[cell_idx].alive = True

        #update cells
        for cell in self.cells:
            cell.update()
        self.stoplight.update()


class Grid:
    def __init__(self, cell_size):
        self.SCREEN_SIZE = pygame.display.get_surface().get_size()
        self.CELL_SIZE = cell_size

        self.cells = []
        self.columns = self.SCREEN_SIZE[0] // self.CELL_SIZE
        self.rows = self.SCREEN_SIZE[1] // self.CELL_SIZE
        
        self.build_cells()

    def build_cells(self):
        for col_idx in range(self.columns):
            for row_idx in range(self.rows):
                self.cells.append(Cell(self.CELL_SIZE, col_idx, row_idx, random.choice([True, False])))
    
    def get_cell(self, col_idx, row_idx):
        for cell in self.cells:
            if cell.column_idx == col_idx and cell.row_idx == row_idx:
                    return cell