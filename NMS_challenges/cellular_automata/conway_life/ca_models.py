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

        blue = random.randint(90, 110)
        self.color = [255-blue, 80, blue]
        self.size = [square_size, square_size]
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        
        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.START_LOC)

        self.alive = living

    def update(self, events_list):
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



        

