import pygame
from pygame.locals import *
import random

class Button(pygame.sprite.Sprite):
    def __init__(self, location=[50, 50], title='blank button'):
        super(Button, self).__init__()

        self.handler = self.default_handler
        self.primary_face = pygame.Surface([100, 60])
        self.rect = self.primary_face.get_rect()

        self.rect.move_ip(location)
        self.primary_face.fill((100, 100, 100))

        self.font = pygame.font.Font(None, 20)
        self.text = self.font.render(title, True, (0, 0, 0))
        self.primary_face.blit(self.text, [0, 0])

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.primary_face, self.rect)

    def default_handler(self):
        print(f'specify button handler function by using object set_handler() method')

    def set_handler(self, special_handler):
        self.handler = special_handler

class Hand:
    def __init__(self, player_human=False):
        self.in_hand = []
        self.win_tally = 0
        self.has_ace = False

        if player_human:
            self.draw_start = [50, 500]
            self.name = 'Player'
        else:
            self.draw_start = [50, 50]
            self.name = 'Computer'

    def add_card(self, card):
        if card.rank == 'Ace': #set has_ace to ace index in in_hand
            self.has_ace = len(self.in_hand)
        self.in_hand.append(card)

    
    def clear_hand(self):
        self.in_hand = []

    @property
    def hand_score(self):
        """Calculate score of Hand, considering variable value of Ace"""
        #calculate score and soften aces as needed
        score = 0
        for card in self.in_hand:
            score += card.points
        if score > 21:
            for card in self.in_hand:
                if card.soften_ace():
                    score -= 10
        return score

    @property
    def bust(self):
        if self.hand_score > 21:
            return True
        return False

    def draw_hand(self):
        for idx, card in enumerate(self.in_hand):
            #draw each card, slightly overlapped, starting from draw_start
            drawx = self.draw_start[0] + idx*card.size[0] // 1.5
            drawy = self.draw_start[1]
            card.draw([drawx, drawy])

    def compare(self, other_hand):
        """Compare self.score to passed Hand considering Blackjack rules"""
        if self.bust:
            if other_hand.bust: #both lose
                print('Everyone loses')
            else: #self lose, other win
                other_hand.win_tally += 1
        elif self.hand_score == other_hand.hand_score: #tie
            self.win_tally += 1
            other_hand.win_tally += 1
            print('Draw')
        else: #self is not bust
            if other_hand.bust: #self win, other lose
                self.win_tally += 1
            else: #both are under 21, comapre
                if self.hand_score > other_hand.hand_score:
                    self.win_tally += 1
                else: #other hand wins
                    other_hand.win_tally += 1


class Deck:
    SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    RANKS = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
    
    def __init__(self):
        self.deck_contents = []
        self.discarded = []
        self.dealt = False

        self.build_deck()

    def draw_deck(self):
        """Render card from top of Deck stack at specified Deck location"""
        try:
            self.deck_contents[-1].draw([100, 300])
        except:
            pass

    def build_deck(self):
        for item in self.RANKS:
            for suit in self.SUITS:
                self.deck_contents.append(Card(item, suit))
    
    def discard(self, card):
        self.discarded.append(self.deck_contents.pop(card))

    def shuffle(self):
        random.shuffle(self.deck_contents)
    
    def deal(self, hand):
        """Transfer Card from Deck to passed Hand"""
        try:
            deal_card = self.deck_contents.pop()
            hand.add_card(deal_card)
        except:
            print('new deck')
            self.__init__()
            self.shuffle()
        

class Card(pygame.sprite.Sprite):
    SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    RANKS = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
    VALUES = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

    def __init__(self, rank, suit):
        super(Card, self).__init__()
        
        self.suit = suit
        self.rank = rank
        self.points = self.VALUES[self.rank]
        self.sheet_cell_idx = self.get_cell_idx()

        self.spritesheet = Spritesheet('card_deck.png', 13, 4)
        self.size = [self.spritesheet.cell_width, self.spritesheet.cell_height]
        self.front_face = pygame.Surface(self.size)
        self.rect = self.front_face.get_rect()
        
        #copy cell surface to front_face
        self.spritesheet.stamp_cell(self.front_face, self.sheet_cell_idx, self.rect)

    def get_points(self):
        return self.points

    def soften_ace(self):
        if self.rank == 'Ace' and self.points == 11:
            self.points == 1
            return True
        return False

    def draw(self, draw_location):
        main_window = pygame.display.get_surface()

        self.rect = self.front_face.get_rect()
        self.rect = self.rect.move(draw_location)
        main_window.blit(self.front_face, self.rect)

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
