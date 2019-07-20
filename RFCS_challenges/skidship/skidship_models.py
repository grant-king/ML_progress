import pygame
from pygame.locals import *
import random
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.ANGLE_INCREMENT = 4
        self.ORIENTATION = 90 # initial ccw rotation of image from right-facing at 0 degrees

        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h

        self.pristine_surface = pygame.image.load('carrot1.png').convert()
        self.pristine_surface.set_colorkey([255, 255, 255])
        
        self.angle = 0
        self.surface = pygame.transform.rotate(self.pristine_surface, self.absolute_rotation)
        
        self.rect = self.surface.get_rect()
        self.acceleration = [0, 0]
        self.velocity = [1, 0]
        self.thrust_coeff = 1.5 # greater than one
        self.friction_coeff = 0.025 # less than one

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
        # absolute clockwise rotation from original heading
        return -(self.ORIENTATION + self.angle)

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
                        #execute indicated function with corresponding command
                        keydown_inputs[key_name][0](keydown_inputs[key_name][1])

    def toggle_thrust(self, thruster_name):
        if thruster_name in self.thrusters.keys():
            if self.thrusters[thruster_name] == True:
                self.thrusters[thruster_name] = False
                print(f'{thruster_name} off')
            else:
                self.thrusters[thruster_name] = True
                print(f'{thruster_name} on')

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


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.ANGLE_INCREMENT = 4

        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h
        
        self.acceleration = [0, 0]
        self.velocity = [random.randint(4, 10), random.randint(0, 4)]
        self.friction_coeff = 0.001 # less than one
        self.angle = 0

        self.spritesheet = Spritesheet('skullchomp.png', 1, 6)
        self.size = [self.spritesheet.cell_width, self.spritesheet.cell_height]
        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey([0, 0, 0]) 
        
        self.rect = self.surface.get_rect()
        self.current_cell_idx = 0
        self.spritesheet.stamp_cell(self.surface, self.current_cell_idx, self.rect)

    @property
    def angle_rads(self):
        return self.angle * 3.14/180

    def update(self, events_list):
        self.contain()
        self.update_vectors()
        self.update_image()
        self.draw()

    def update_image(self):
        #clear surface
        self.surface.fill([0, 0, 0])
        #stamp next image to surface
        self.spritesheet.stamp_cell(self.surface, self.current_cell_idx, [0, 0, 150, 150])
        
        #update cell idx in relation to current x position on main screen
        self.current_cell_idx = (self.rect.x // 20) % self.spritesheet.num_rows

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_vectors(self):
        #update velocity with friction
        self.velocity[0] *= (1 - self.friction_coeff)
        self.velocity[1] *= (1 - self.friction_coeff)
    
        self.velocity[0] += self.acceleration[0] 
        self.velocity[1] += self.acceleration[1]

        #update rectangular position
        self.rect.move_ip(self.velocity)

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

class Spritesheet:
    def __init__(self, filename, num_cols, num_rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet.convert()

        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_count = num_cols * num_rows

        self.rect = self.sheet.get_rect()
        self.cell_width = self.rect.width / self.num_cols
        self.cell_height = self.rect.height / self.num_rows

        #get x y offset for start of each cell
        self.offset_list = []
        for index in range(self.cell_count):
            x_offset = int(index % self.num_cols * self.cell_width)
            y_offset = int(index // self.num_cols * self.cell_height)
            #append items as rect constructor
            self.offset_list.append((x_offset, y_offset, self.cell_width, self.cell_height))

    def stamp_cell(self, destination, cell_index, draw_location):
        source_area = self.offset_list[cell_index]

        destination.blit(self.sheet, draw_location, area=source_area)