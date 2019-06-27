import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surface = pygame.image.load('circle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.position.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.position.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.position.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.position.move_ip(5, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.surface = pygame.image.load('circle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect()
        self.velocity = [11, 1]

    def update(self, pressed_keys):
        self.control(pressed_keys)
        self.bounce()
        self.position.move_ip(self.velocity)
    
    def control(self, pressed_keys):
        if pressed_keys[K_RIGHT]:
            self.velocity[0] += 1
        if pressed_keys[K_LEFT]:
            self.velocity[0] += -1
        if pressed_keys[K_DOWN]:
            self.velocity[1] += 1
        if pressed_keys[K_UP]:
            self.velocity[1] += -1


    def bounce(self):
        if self.position.midleft[0] < 0 or self.position.midright[0] > 500:
            self.velocity[0] = -self.velocity[0]
        if self.position.midtop[1] < 0 or self.position.midbottom[1] > 500:
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
main_window = pygame.display.set_mode((500, 500))

player = Player()
ball = Ball()
running = True

clock = pygame.time.Clock()

while running:
    running = listen_quit()
    clock.tick(60)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    ball.update(pressed_keys)

    main_window.fill((0, 0, 0))
    main_window.blit(player.surface, player.position)
    main_window.blit(ball.surface, ball.position)

    pygame.display.flip()        

    