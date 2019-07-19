import pygame
from pygame.locals import *
import random
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h

        self.pristine_surface = pygame.image.load('sled.png').convert()
        self.pristine_surface.set_colorkey([0, 0, 0])
        
        self.angle = 0
        #initial ccw rotation of image from right-facing at 0 degrees
        self.orient = 90
        self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)
        
        self.rect = self.surface.get_rect()
        self.acceleration = [0, 0]
        self.velocity = [1, 0]
        self.thrust_coeff = 1.5 #greater than one
        self.friction_coeff = 0.01 #less than one

        self.thrust = False

    @property
    def angle_rads(self):
        return self.angle * 3.14/180

    def update(self, events_list):
        self.control(events_list)
        self.contain()
        self.update_vectors() 
        self.constrain_attributes()
        self.draw()

    def constrain_attributes(self):
        ACC_LIMIT = 3
        VELOCITY_LIMIT = 20
        
        #constrain acceleration
        for item in self.acceleration:
            if item > ACC_LIMIT:
                item = ACC_LIMIT
        #constrain velocity
        for item in self.velocity:
            if item > VELOCITY_LIMIT:
                item = VELOCITY_LIMIT

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_vectors(self):
        #update velocity with friction
        self.velocity[0] *= (1 - self.friction_coeff)
        self.velocity[1] *= (1 - self.friction_coeff)

        #update acceleration with thrust and add to velocity
        if self.thrust:
            self.acceleration[0] = math.cos(self.angle_rads) * self.thrust_coeff
            self.acceleration[1] = math.sin(self.angle_rads) * self.thrust_coeff
        else:
            self.acceleration = [0, 0]

        self.velocity[0] += self.acceleration[0] 
        self.velocity[1] += self.acceleration[1]

        #update rectangular position
        self.rect.move_ip(self.velocity)

    @property
    def absolute_rotation(self):
        #absolute clockwise rotation from original heading
        return -(self.orient + self.angle)

    def control(self, events_list):
        ANGLE_INCREMENT = 15
        ##todo make controls continuous, reset thrust when no input
        for event in events_list:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.thrust = True
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_LEFT:
                    #rotate ccw
                    self.angle -= ANGLE_INCREMENT
                    self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)
                elif event.key == K_RIGHT:
                    #rotate clockwise
                    self.angle += ANGLE_INCREMENT
                    self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)
                else:
                    print(f'{event.key} key press')
                print(self)
                
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.thrust = False
                elif event.key == K_DOWN:
                    pass
                else:
                    print(f'{event.key} key lift')
                print(self)

    def contain(self):
        size = 70
        #portal walls
        ##todo change to use rect center
        if self.rect.midtop[1] < -size:
            self.rect.move_ip(0, self.max_y)
        if self.rect.midbottom[1] > self.max_y + size:
            self.rect.move_ip(0,  -(self.max_y + size))
        if self.rect.midleft[0] < -size:
            self.rect.move_ip(self.max_x, 0)
        if self.rect.midright[0] > self.max_x + size:
            self.rect.move_ip(-(self.max_x + size), 0)

    def __str__(self):
        accx = f'{self.acceleration[0]:.2f}'
        accy = f'{self.acceleration[1]:.2f}'
        return f'acc: {accx, accy} || vel: {self.velocity} || angle: {self.angle} || thrust: {self.thrust}'
