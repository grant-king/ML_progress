import pygame
from pygame.locals import *
import random

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h

        self.surface = pygame.Surface([60, 60])
        self.rect = self.surface.get_rect()
        
        self.surface.fill([50, 10, 10])

        self.velocity = [1, 7]

    def update(self, events_list):
        self.control(events_list)
        self.contain()
        self.update_vectors()
        self.draw()

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_vectors(self):
        self.rect.move_ip(self.velocity)

    def control(self, events_list):
        for event in events_list:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass
                else:
                    print(f'{event.key} key pressed')

    def contain(self):
        #reflect off of walls
        if self.rect.midtop[1] < 0:
            self.velocity[1] = -self.velocity[1]
            self.rect.move_ip(0, 10)
        if self.rect.midbottom[1] > self.max_y:
            self.velocity[1] = -self.velocity[1]
            self.rect.move_ip(0, -10)
        if self.rect.midleft[0] < 0:
            self.velocity[0] = -self.velocity[0]  
            self.rect.move_ip(10, 0)
        if self.rect.midright[0] > self.max_x:
            self.velocity[0] = -self.velocity[0]
            self.rect.move_ip(-10, 0)

