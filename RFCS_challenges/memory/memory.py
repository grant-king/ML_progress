import pygame
from pygame.locals import *
import random

class Card(pygame.sprite.Sprite):
    def __init__(self):
        super(Card, self).__init__()
        self.max_x = pygame.display.Info().current_h
        self.max_y = pygame.display.Info().current_w

        #self.front_face = pygame.image.load(imagefile)
        self.back_face = pygame.image.load('cardback.png').convert()
        self.active_face = self.back_face

        spawnx = random.randint(0, self.max_x)
        spawny = random.randint(0, self.max_y)
        print(spawnx, spawny)
        self.rect = self.back_face.get_rect(center=(spawnx, spawny))
        
        self.velocity = [1, 1]   

    def update(self):
        self.contain()
        self.rect.move_ip(self.velocity)

    def control(self):
        pass

    def contain(self):
        #reflect off of walls
        if self.rect.midtop[1] < 0:
            self.velocity[1] = -self.velocity[1]
        if self.rect.midbottom[1] > self.max_y:
            self.velocity[1] = -self.velocity[1]
        if self.rect.midleft[0] < 0:
            self.velocity[0] = -self.velocity[0]  
        if self.rect.midright[0] > self.max_x:
            self.velocity[0] = -self.velocity[0]

    def bounce_handler(self):
        self.velocity = [-self.velocity[0], -self.velocity[1]]

def listen_quit():
    #listen for quit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

pygame.init()
main_window = pygame.display.set_mode((600, 600))
cards = [Card() for card in range(16)]
all_sprites = pygame.sprite.Group()
all_sprites.add(cards)

running = True
clock = pygame.time.Clock()

while running:
    running = listen_quit()
    clock.tick(60)
    main_window.fill((0, 0, 0))

    for entity in all_sprites:
        #check collisions
        card_collides = pygame.sprite.spritecollideany(entity, all_sprites)
        if type(card_collides) is Card:
            entity.bounce_handler()
            card_collides.bounce_handler()
        #update sprites and draw
        entity.update()
        main_window.blit(entity.active_face, entity.rect)
    
    pygame.display.flip()