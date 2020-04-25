import pygame
from pygame.locals import *
import random

class Card(pygame.sprite.Sprite):
    def __init__(self):
        super(Card, self).__init__()
        self.max_x = pygame.display.Info().current_w
        self.max_y = pygame.display.Info().current_h
        
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

def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

def compare(compare_list):
    if compare_list[0].color == compare_list[1].color:
        return True
    return False

def draw_stats(score, matches):
    main_window = pygame.display.get_surface()
    
    font = pygame.font.Font(None, 50)
    message = f'{score} clicks and {matches} matches'
    text = font.render(message, True, (255, 255, 0))

    main_window.blit(text, [main_window.get_rect().width/2-200, 50])

def draw_end():
    main_window = pygame.display.get_surface()
    
    font = pygame.font.Font(None, 150)
    message = 'You win!'
    text = font.render(message, True, (255, 55, 55))

    main_window.blit(text, [main_window.get_rect().width/2-200, main_window.get_rect().height/2])

MATCH_NUMBER = 7

pygame.init()
main_window = pygame.display.set_mode((600, 600))
cards = [Card() for card in range(MATCH_NUMBER * 2)]
matches = [Match(cards[i], cards[i+1]) for i in range(len(cards))[::2]]
all_sprites = pygame.sprite.Group()
all_sprites.add(cards)

running = True

score = 0
to_compare = [] #up to two cards
matched = [] #all successfully compared, stay face up
locked = [] #unmatched to be flipped to cardback after new try

clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(60)
    main_window.fill((0, 0, 0))

    click_pos = None
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            click_pos = event.pos

    running = listen_quit(events)
    
    for card in all_sprites:
        #check clicks
        if click_pos:
            if card.rect.collidepoint(click_pos):
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
    
    #draw stats
    draw_stats(score, len(matched))
    
    #update display
    pygame.display.flip()
    
    #game logic
    if click_pos != None:
        score += 1
        if len(to_compare) == 2:
            match = compare(to_compare)
            if match:
                #save cards to matched list
                _ = [matched.append(item) for item in to_compare]
                print('match')
            else:
                #save cards to flipped list
                _ = [locked.append(item) for item in to_compare]
                print('no match')
            #reset
            to_compare.clear()
        elif len(to_compare) == 1: 
        #flip mismatched cards after first new choice
            if len(locked) == 2:
                locked[0].active_face =  locked[0].back_face
                locked[1].active_face =  locked[1].back_face
                locked.clear()
        else:
            pass

    if len(matched) == MATCH_NUMBER*2:
        draw_end()
        pygame.display.flip()
        pygame.time.delay(3500)
        running = False
    