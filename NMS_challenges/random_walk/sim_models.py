import pygame
from pygame.locals import *
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()
        
        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h
        
        self.COLOR = [random.randrange(50, 200), 10, random.randrange(20, 50)]
        self.START_LOC = [self.max_x/2, self.max_y/2]

        self.size = [1, random.randrange(1, 100)]
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.COLOR)
        
        self.rect = self.surface.get_rect(center=self.START_LOC)

    def update(self, events_list):
        self.walk()
        self.draw()

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def walk(self):
        move_x = random.randrange(1, 10)
        move_y = random.randrange(1, 10)

        options = {
            'North': (lambda: self.rect.move_ip(0, -move_y)),
            'East': (lambda: self.rect.move_ip(move_x, 0)),
            'South': (lambda: self.rect.move_ip(0, move_y)),
            'West': (lambda: self.rect.move_ip(-move_x, 0)),
            }

        direction = random.choice(list(options.keys()))
        options[direction]()
        
        