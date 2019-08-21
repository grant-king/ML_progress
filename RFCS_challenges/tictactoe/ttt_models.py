import pygame
from pygame.locals import *
import random

class Grid:
    def __init__(self):
        self.ROWS = 3 
        self.COLS = 3

        self.cells = [[Cell([row, column]) for row in range(self.ROWS)] for column in range(self.COLS)]

        self.cell_size = self.cells[0][0].size
        self.size = [self.cell_size[0] * self.COLS, self.cell_size[1] * self.ROWS]
        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect()
        
        self.generate_overlay()

    def draw(self):
        main_window = pygame.display.get_surface()

        #draw cells and contents
        for cell_row in self.cells:
            for cell in cell_row:
                cell.draw(self.surface)
        
        #add overlay
        self.surface.blit(self.border_overlay, self.rect)

        #draw composite on main display
        main_window.blit(self.surface, self.rect)

    def play(self, symbol, grid_idx):
        cell = self.cells[grid_idx[0]][grid_idx[1]]
        cell.occupy(symbol)

    def generate_overlay(self):
        overlay_color = [100, 100, 100]
        overlay_surface = pygame.Surface(self.size)
        overlay_surface.set_colorkey([0, 0, 0])
        line_width = 10

        vert_line_separation = self.size[0] // self.COLS
        horiz_line_separation = self.size[1] // self.ROWS
        
        for row in range(1, self.ROWS):
            start_pos = [0, row*horiz_line_separation]
            end_pos = [self.size[0], row*horiz_line_separation]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        for col in range(1, self.COLS):
            start_pos = [col*vert_line_separation, 0]
            end_pos = [col*vert_line_separation, self.size[1]]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        self.border_overlay = overlay_surface


class Cell:
    def __init__(self, grid_idx):
        self.grid_idx = grid_idx
        self.size = [100, 100]
        self.coordinate_location = [grid_idx[0] * self.size[0], grid_idx[1] * self.size[1]]

        self.occupied = False

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


