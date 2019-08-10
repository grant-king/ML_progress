import pygame
from pygame.locals import *
import random

class Particle(pygame.sprite.Sprite):
    VELOCITIES = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def __init__(self, lat_x, lat_y):
        super(Particle, self).__init__()
        self.velocity = random.choice(self.VELOCITIES)
        self.location = [lat_x, lat_y] #vertex coordinates of lattice
        

class Lattice:
    def __init__(self, edge_spacing):
        self.WINDOW_SIZE = pygame.display.get_surface().get_size()
        self.SPACING = edge_spacing

    def update(self):
        self.collision_step()
        self.draw()

    def collision_step(self):
        for x_edge in self.x_edges:
            for y_edge in self.y_edges:
                pass
                
    def draw(self):



