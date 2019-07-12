import pygame
from pygame.locals import *
import random

class Card(pygame.sprite.Sprite):
    SUITS = ('C', 'S', 'H', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

    def __init__(self, suit, rank):
        super(Card, self).__init__()
        
        self.suit = suit
        self.rank = rank

        self.spritesheet = Spritesheet('card_deck.png', 13, 4)
        self.size = [self.spritesheet.cell_width, self.spritesheet.cell_height]
        self.front_face = pygame.Surface(self.size)
        self.rect = self.front_face.get_rect()
        
        #copy cell surface to front_face
        self.spritesheet.draw(self.front_face, 0, self.rect)

    def __str__(self):
        return f'{self.suit} {self.rank}'



class Spritesheet:
    def __init__(self, filename, num_cols, num_rows):
        self.sheet = pygame.image.load(filename).convert_alpha()

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

    def draw(self, surface, cell_index, draw_location):
        source = self.sheet
        source_area = self.offset_list[cell_index]

        surface.blit(source, draw_location, area=source_area)


def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

pygame.init()
main_window = pygame.display.set_mode((600, 600))

card = Card(1, 2)

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(10)
    main_window.fill((0, 0, 0))

    running = listen_quit(events)

    card_img_idx = random.randint(0, 51)
    main_window.blit(card.front_face, card.rect)

    pygame.display.flip()
