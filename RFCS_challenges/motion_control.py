import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surface = pygame.Surface((50, 50))
        self.surface.fill((0, 255, 50))
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

pygame.init()
main_window = pygame.display.set_mode((500, 500))

player = Player()
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
    player.update(pressed_keys)

    main_window.fill((0, 0, 0))
    main_window.blit(player.surface, player.position)
    pygame.display.flip()        

    