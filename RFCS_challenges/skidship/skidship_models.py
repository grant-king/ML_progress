import pygame
from pygame.locals import *
import random
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.ANGLE_INCREMENT = 4

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
        self.friction_coeff = 0.025 #less than one

        self.thrusters = {
            'thrust': False,
            'rthrust': False,
            'lthrust': False,
        }
        
    @property
    def angle_rads(self):
        return self.angle * 3.14/180

    @property
    def absolute_rotation(self):
        #absolute clockwise rotation from original heading
        return -(self.orient + self.angle)

    def update(self, events_list):
        self.control(events_list)
        self.contain()
        self.update_vectors() 
        self.draw()

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_vectors(self):
        #update velocity with friction
        self.velocity[0] *= (1 - self.friction_coeff)
        self.velocity[1] *= (1 - self.friction_coeff)

        ##### fix to work with continuous 3 thruster control scheme
            
        #update acceleration with thrust and add to velocity
        if self.thrusters['thrust']:
            self.acceleration[0] = math.cos(self.angle_rads) * self.thrust_coeff
            self.acceleration[1] = math.sin(self.angle_rads) * self.thrust_coeff
        else:
            self.acceleration = [0, 0]

        if self.thrusters['rthrust']:
            self.angle -= self.ANGLE_INCREMENT
            self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)

        if self.thrusters['lthrust']:
            self.angle += self.ANGLE_INCREMENT
            self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)

        #####

        self.velocity[0] += self.acceleration[0] 
        self.velocity[1] += self.acceleration[1]

        #update rectangular position
        self.rect.move_ip(self.velocity)

    def control(self, events_list):
        keydown_inputs = {
            K_UP: [self.toggle_thrust, 'thrust'],
            K_LEFT: [self.toggle_thrust, 'rthrust'],
            K_RIGHT: [self.toggle_thrust, 'lthrust'],
        }

        for event in events_list:
            if event.type == KEYDOWN or event.type == KEYUP:
                for key_name in keydown_inputs.keys():
                    if event.key == key_name:
                        #execute function with command
                        keydown_inputs[key_name][0](keydown_inputs[key_name][1])
                print(self)
    
    def rotate_cw(self):
        ANGLE_INCREMENT = 15
        self.angle += ANGLE_INCREMENT
        self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)

    def rotate_ccw(self):
        pass
        

    def toggle_thrust(self, thruster_name):
        thruster_names = ['thrust', 'rthrust', 'lthrust']

        if thruster_name in thruster_names:
            for idx, thruster in enumerate(self.thrusters):
                if self.thrusters[thruster_name] == True:
                    self.thrusters[thruster_name] = False
                    print('thruster off')
                else:
                    self.thrusters[thruster_name] = True
                    print('thruster on')

    def contain(self):
        #portal walls
        if self.rect.centery < 0:
            self.rect.move_ip(0, self.max_y)
        if self.rect.centery > self.max_y:
            self.rect.move_ip(0,  -(self.max_y))
        if self.rect.centerx < 0:
            self.rect.move_ip(self.max_x, 0)
        if self.rect.centerx > self.max_x:
            self.rect.move_ip(-(self.max_x), 0)    
                    
    def __str__(self):
        accx = f'{self.acceleration[0]:.2f}'
        accy = f'{self.acceleration[1]:.2f}'
        return f'acc: {accx, accy} || vel: {self.velocity} || angle: {self.angle} || thrust: {self.thrusters["thrust"]}'


