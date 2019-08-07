import pygame
from pygame.locals import *
import random

class Particle(pygame.sprite.Sprite):
    VELOCITIES = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def __init__(self, lat_x, lat_y):
        super(Particle, self).__init__()
        self.velocity = random.choice(self.VELOCITIES)
        self.location = [lat_x, lat_y] #vertex coordinates of lattice


class Edge:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Lattice:
    def __init__(self, edge_spacing):
        self.WINDOW_SIZE = pygame.display.get_surface().get_size()
        self.SPACING = edge_spacing
        num_edges = self.WINDOW_SIZE[0] // self.SPACING
        #coordinates for vertical edge location
        self.x_edges = [Edge([x, 0]) for x in range(0, self.WINDOW_SIZE, self.SPACING)]
        self.y_edges = [Edge(0, y) for y in range(0, self.WINDOW_SIZE, self.SPACING)]

    def update(self):
        self.collision_step()

    def collision_step(self):
        for x_edge in self.x_edges:
            for y_edge in self.y_edges:
                pass
                


