import pygame
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()

        self.image = pygame.image.load('circle.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.position = self.image.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.position.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.position.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.position.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.position.move_ip(5, 0)

pygame.init()
main_window = pygame.display.set_mode((500, 500))

ball = Ball()
running = True

clock = pygame.time.Clock()

while running:
    #listen for quit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    clock.tick(60)

    pressed_keys = pygame.key.get_pressed()
    ball.update(pressed_keys)

    main_window.fill((0, 0, 0))
    main_window.blit(ball.image, ball.position)
    pygame.display.flip()        

    