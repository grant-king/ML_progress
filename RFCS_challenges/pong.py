import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, player_int):
        super(Player, self).__init__()

        self.surface = pygame.image.load('paddle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect(center=(x_pos, 50))
        self.player_int = player_int
        
    def update(self, pressed_keys, window):
        self.control(pressed_keys)
        self.contain(window)
    
    def control(self, pressed_keys):
        if self.player_int == 2:
            if pressed_keys[K_UP]:
                self.position.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.position.move_ip(0, 5)
        if self.player_int == 1:
            if pressed_keys[K_w]:
                self.position.move_ip(0, -5)
            if pressed_keys[K_s]:
                self.position.move_ip(0, 5)

    def contain(self, window):    
        if self.position.midtop[1] < 0:
            self.position.move_ip(0, 10)
        if self.position.midbottom[1] > window.get_height():
            self.position.move_ip(0, -10)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surface = pygame.image.load('circle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect()
        self.velocity = [11, 1]

    def update(self, pressed_keys, window):
        self.control(pressed_keys)
        self.bounce(window)
        self.position.move_ip(self.velocity)
    
    def control(self, pressed_keys):
        if pressed_keys[K_KP_PLUS]:
            self.velocity[0] += 1
        if pressed_keys[K_KP_MINUS]:
            self.velocity[0] += -1

    def bounce(self, window):
        if self.position.midleft[0] < 0 or self.position.midright[0] > window.get_width():
            self.velocity[0] = -self.velocity[0]
        if self.position.midtop[1] < 0 or self.position.midbottom[1] > window.get_height():
            self.velocity[1] = -self.velocity[1]           


def listen_quit():
    #listen for quit
    running = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    return running

pygame.init()
main_window = pygame.display.set_mode((1200, 900))

player1 = Player(50, 1)
player2 = Player(1180, 2)
ball = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, ball)

running = True
clock = pygame.time.Clock()

while running:
    running = listen_quit()
    clock.tick(60)

    pressed_keys = pygame.key.get_pressed()
    main_window.fill((0, 0, 0))

    for entity in all_sprites:
        entity.update(pressed_keys, main_window)
        main_window.blit(entity.surface, entity.position)
    
    pygame.display.flip()

    