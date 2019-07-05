import pygame
from pygame.locals import *
import random

class Card(pygame.sprite.Sprite):
    def __init__(self):
        super(Card, self).__init__()
        self.max_x = pygame.display.Info().current_h
        self.max_y = pygame.display.Info().current_w
        
        self.color = [1, 1, 1]
        self.front_face = pygame.Surface([60, 60])
        self.back_face = pygame.image.load('cardback.png').convert()
        self.active_face = self.back_face

        spawnx = random.randint(0, self.max_x)
        spawny = random.randint(0, self.max_y)
        self.rect = self.active_face.get_rect(center=(spawnx, spawny))
        
        self.velocity = [0, 1]   

    def update(self):
        self.control()
        self.contain()
        self.rect.move_ip(self.velocity)

    def control(self):
        pass

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

    def bounce_handler(self):
        self.velocity = [-self.velocity[0], -self.velocity[1]]

    def click_handler(self):
        if self.active_face == self.back_face:
            self.active_face = self.front_face

class Match:
    def __init__(self, card_1, card_2):
        self.found = False
        self.color = [0, 0, 0]
        self.card_base = card_1
        self.card_copy = card_2
        self.match_maker()
    
    def match_maker(self):
        r, g, b = [random.randint(0, 255) for i in range(3)]
        self.card_base.front_face.fill((r, g, b))
        self.card_copy.front_face.fill((r, g, b))
        self.card_base.color = [r, g, b]
        self.card_copy.color = [r, g, b]
        self.color = [r, g, b]

def listen_quit():
    #listen for quit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

def get_click_pos():
    click = pygame.mouse.get_pressed()
    click_pos = None
    if click[0]:
        click_pos = pygame.mouse.get_pos()
        #wait for mouse up
        for event in pygame.event.get():
            while event.type == pygame.MOUSEBUTTONDOWN:
                print('waiting')
    return click_pos

def compare(compare_list):
    if compare_list[0].color == compare_list[1].color:
        return True
    return False

pygame.init()
main_window = pygame.display.set_mode((600, 600))
cards = [Card() for card in range(6)]
matches = [Match(cards[i], cards[i+1]) for i in range(len(cards))[::2]]
all_sprites = pygame.sprite.Group()
all_sprites.add(cards)

running = True

to_compare = []#up to two cards
matched = []#all successfully compared, stay face up
clock = pygame.time.Clock()

while running:
    running = listen_quit()
    clock.tick(60)
    main_window.fill((0, 0, 0))

    click_pos = get_click_pos()

    for card in all_sprites:
        #check clicks
        if click_pos:
            if card.rect.collidepoint(click_pos):
                for couples in matched:
                    if card not in couples:
                        card.click_handler() 
                if card not in to_compare:
                    to_compare.append(card)
        #check collisions
        card_collides = pygame.sprite.spritecollideany(card, all_sprites)
        if type(card_collides) is Card:
            card.bounce_handler()
            card_collides.bounce_handler()
        #update sprites and draw
        card.update()
        main_window.blit(card.active_face, card.rect)
    
    #update display
    pygame.display.flip()
    
    #game logic
    if click_pos != None:
        if len(to_compare) == 2:
            print(to_compare)
            match = compare(to_compare)
            if match:
                matched.append(to_compare.copy())
                print('match')
            else:
                to_compare[0].active_face =  to_compare[0].back_face
                to_compare[1].active_face =  to_compare[1].back_face
                print('no match')
            #reset
            to_compare.clear()
        
    