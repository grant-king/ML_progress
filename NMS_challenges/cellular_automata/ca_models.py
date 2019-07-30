import pygame
from pygame.locals import *
import random

class Cell(pygame.sprite.Sprite):
    def __init__(self, startx, starty, living=False):
        super(Cell, self).__init__()
        
        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h
        
        self.START_LOC = [startx, starty]

        self.color = [120, 120, 100]
        self.size = [50, 50]
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


