from game_models import *

def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

def hit_handler(player_hand, dealer_hand):
    global deck
    deck.deal(player_hand)
    print(f'Player: {player_hand.hand_score}')

def deal_handler(player_hand, dealer_hand):
    global deck
    if not deck.dealt:
        deck.deal(player_hand)
        deck.deal(dealer_hand)
        deck.dealt = True

def stand_handler(player_hand, dealer_hand):
    global deck
    #fill dealer hand
    dealer_hit(dealer_hand)
    
    #compare hands
    player_hand.compare(dealer_hand)

    #print stats and clear hands
    for hand in [player_hand, dealer_hand]:
        print(f'{hand.name}: {hand.win_tally}')
        hand.clear_hand()
    deck.dealt = False
    
def dealer_hit(dealer_hand):
    while dealer_hand.hand_score < 17:
        deck.deal(dealer_hand)
        print(f'Dealer: {dealer_hand.hand_score}')

pygame.init()
main_window = pygame.display.set_mode((900, 600))

deck = Deck()
deck.shuffle()
dealer_hand = Hand()
player_hand = Hand(True)

deal_button = Button([350, 250], 'deal') # shuffle deck and deal card to each player
hit_button = Button([350, 325], 'hit') # add card to current player
stand_button = Button([350, 400], 'stand')
deal_button.set_handler(deal_handler)
hit_button.set_handler(hit_handler)
stand_button.set_handler(stand_handler)

#create sprite groups
card_sprites = pygame.sprite.Group()
card_sprites.add(deck.deck_contents)

button_sprites = pygame.sprite.Group()
button_sprites.add([deal_button, hit_button, stand_button])

all_sprites = pygame.sprite.Group()
all_sprites.add([card_sprites, button_sprites])

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(60)
    main_window.fill((20, 100, 20))

    running = listen_quit(events)

    click_pos = None
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            click_pos = event.pos

    for button in button_sprites:
        if click_pos:
            if button.rect.collidepoint(click_pos):
                button.handler(player_hand, dealer_hand)
        button.draw()

    deck.draw_deck()

    player_hand.draw_hand()
    dealer_hand.draw_hand()

    pygame.display.flip()
