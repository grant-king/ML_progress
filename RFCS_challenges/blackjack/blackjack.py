import pygame
from pygame.locals import *
import random

class Hand:
    def __init__(self):
        self.in_hand = []

    def add_card(self, card):
        self.in_hand.append(card)

    @property
    def score(self):
        score = 0
        for card in self.in_hand:
            score += card.points


class Deck:
    SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    RANKS = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
    
    def __init__(self):
        self.deck_contents = []
        self.discarded = []

        self.build_deck()

    def build_deck(self):
        for item in self.RANKS:
            for suit in self.SUITS:
                self.deck_contents.append(Card(item, suit))
    
    def discard(self, card):
        self.discarded.append(self.deck_contents.pop(card))


class Card(pygame.sprite.Sprite):
    SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    RANKS = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
    VALUES = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

    def __init__(self, rank, suit):
        super(Card, self).__init__()
        
        self.suit = suit
        self.rank = rank
        self.sheet_cell_idx = self.get_cell_idx()

        self.spritesheet = Spritesheet('card_deck.png', 13, 4)
        self.size = [self.spritesheet.cell_width, self.spritesheet.cell_height]
        self.front_face = pygame.Surface(self.size)
        self.rect = self.front_face.get_rect()
        
        #copy cell surface to front_face
        self.spritesheet.stamp_cell(self.front_face, self.sheet_cell_idx, self.rect)

    @property
    def points(self):
        return self.VALUES[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}, worth {self.points} points'

    def get_cell_idx(self):
        cell_index = self.SUITS.index(self.suit) * len(self.RANKS) + self.RANKS.index(self.rank)
        return cell_index

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

    def stamp_cell(self, destination, cell_index, draw_location):
        source_area = self.offset_list[cell_index]

        destination.blit(self.sheet, draw_location, area=source_area)


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

#card = Card('Two', 'Hearts')
deck = Deck()

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(1)
    main_window.fill((0, 0, 0))

    running = listen_quit(events)

    card = random.choice(deck.deck_contents)
    print(card)
    main_window.blit(card.front_face, card.rect)

    pygame.display.flip()
