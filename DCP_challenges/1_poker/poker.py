"""Write a program to compare poker hands"""

import random

def get_new_deck(shuffle=True):
    """"return a list containing the unshuffled cards of a new deck, 
    represented as two-character strings, ie 'QH'"""
    deck = [f'{rank}{suit}' for rank in '23456789TJQKA' for suit in 'SHDC']
    if shuffle:
        random.shuffle(deck)
    return deck

def deal(num_hands, cards_per=5, deck=get_new_deck()):
    hands = []
    for hand in range(num_hands):
        hand = []
        for card in range(cards_per):
            if len(deck) > 0:
                hand.append(deck.pop(0))
            else:
                deck = get_new_deck()
                hand.append(deck.pop(0))

        hands.append(hand)
    return hands

def best_hand(hands):
    """return the best hand from hands hand list"""
    return get_winning_hands(hands, key=rank_hand)

def get_winning_hands(hands, key=None):
    """return a list of winning poker hands from input hands, according 
    to the key"""
    winning_hands = []
    hand_ranks = sorted(hands, key=key, reverse=True)
    high_rank = hand_ranks[0]
    winning_hands.append(high_rank)
    for hand_rank in hand_ranks[1:]:
        if hand_rank == high_rank:
            winning_hands.append(high_rank)
    return winning_hands

def get_hand_frequencies(number_trials=700000):
    score_frequencies = {} #score category values with their counts
    all_hands = deal(number_trials)
    category_names = [
        'High Card', 'Pair', 'Two Pair', 'Three Kind', 'Straight', 'Flush', 
        'Full House', 'Four Kind', 'Straight Flush', 'Five Kind'
        ]
    scores = [rank_hand(hand) for hand in all_hands] #full score values; category and sub ranking values
    score_categories = [score[0] for score in scores] #score category values only
    unique_categories = set(score_categories)
    for score_category_value in unique_categories:
        frequency = score_categories.count(score_category_value) / number_trials * 100
        score_frequencies[category_names[score_category_value]] = f'{frequency:.4f}%'

    return score_frequencies
    
def rank_hand(hand):
    """return a value to represent the hand's absolute rank"""
    ranks = extract_ranks(hand)
    if is_of_kind(5, ranks):
        return (9, is_of_kind(5, ranks))
    if is_straight(ranks) and is_flush(hand):
        return (8, max(ranks))
    elif is_of_kind(4, ranks):
        return (7, is_of_kind(4, ranks), is_of_kind(1, ranks))
    elif is_of_kind(3, ranks) and is_of_kind(2, ranks):
        return (6, is_of_kind(3, ranks), is_of_kind(2, ranks))
    elif is_flush(hand):
        return (5, *ranks)
    elif is_straight(ranks):
        return (4, *ranks)
    elif is_of_kind(3, ranks):
        return (3, *ranks)
    elif is_two_pair(ranks):
        return (2, *ranks)
    elif is_of_kind(2, ranks):
        return (1, *ranks)
    else:
        return (0, *ranks)

def extract_ranks(hand):
    """return sorted list of card ranks as ints from hand, without the 
    suit. Ace may be high or low."""
    substitutions = {
        'T': '10',
        'J': '11',
        'Q': '12',
        'K': '13',
        'A': '14',
    }
    ranks = [card[0] for card in hand]
    for idx, card_rank in enumerate(ranks):
        if card_rank in substitutions.keys():
            ranks[idx] = substitutions[card_rank]
    ranks = sorted(map(int, ranks), reverse=True)
    if ranks == [14, 5, 4, 3, 2]: #check for ace low straight
        return [5, 4, 3, 2, 1]
    return ranks

def is_straight(card_ranks):
    """return True if card_ranks form a straight, or False otherwise"""
    for idx, card_rank in enumerate(card_ranks[:-1]):
        if card_rank - 1 == card_ranks[idx + 1]:
            pass
        else:
            return False

    return True

def is_flush(hand):
    """return True if all items in hand are in the same suit"""
    suit = hand[0][1]
    flush_counter = 1
    for card in hand[1:]:
        if card[1] == suit:
            flush_counter += 1
    if flush_counter == 5:
        return True
    else:
        return False

def is_of_kind(target_size, card_ranks):
    """return rank of like cards if hand contains target_size repeated rank 
    values within card_ranks, or False otherwise"""
    for card_rank in card_ranks:
        if card_ranks.count(card_rank) == target_size:
            return card_rank

def is_two_pair(card_ranks):
    """return tuple of ranks (highest, lowest) if two pairs are found, 
    or False otherwise."""
    pair_ranks = []
    for unique_rank in set(card_ranks):
        if card_ranks.count(unique_rank) == 2:
            pair_ranks.append(unique_rank)
    
    if len(pair_ranks) == 2:
        return tuple(pair_ranks)
    else:
        return False

def test():
    """test cases for poker program"""
    straight_flush = "6C 7C 8C 9C TC".split()
    four_kind = "9D 9H 9S 9C 7D".split()
    full_house = "TD TC TH 7C 7D".split()
    two_pair = "5S 5D 9H 9C 6S".split()
    four_kind_ranks = extract_ranks(four_kind)
    two_pair_ranks = extract_ranks(two_pair)

    assert best_hand([straight_flush, four_kind, full_house]) == [straight_flush]
    assert best_hand([full_house, four_kind]) == [four_kind]
    assert best_hand([full_house, full_house]) == [full_house, full_house]
    assert best_hand([straight_flush]) == [straight_flush]
    assert best_hand([straight_flush for i in range(100)]) == [straight_flush for i in range(100)]
    assert rank_hand(straight_flush) == (8, 10)
    assert rank_hand(four_kind) == (7, 9, 7)
    assert rank_hand(full_house) == (6, 10, 7)
    assert extract_ranks(straight_flush) == [10, 9, 8, 7, 6]
    assert extract_ranks(four_kind) == [9, 9, 9, 9, 7]
    assert extract_ranks(full_house) == [10, 10, 10, 7, 7]
    assert is_straight([9, 8, 7, 6, 5]) == True
    assert is_straight([9, 8, 8, 6, 5]) == False
    assert is_flush(straight_flush) == True
    assert is_flush(four_kind) == False
    assert is_of_kind(4, four_kind_ranks) == 9
    assert is_of_kind(3, four_kind_ranks) == None
    assert is_of_kind(2, four_kind_ranks) == None
    assert is_of_kind(1, four_kind_ranks) == 7
    assert is_two_pair(two_pair_ranks) == (9, 5)

    print('All tests passed.')

test()
freqencies = get_hand_frequencies(700000)
for key, value in freqencies.items():
    print(f'{key}: {value}')
