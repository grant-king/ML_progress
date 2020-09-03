"""Write a program to compare poker hands"""

def best_hand(hands):
    """return the best hand from hands hand list"""
    return max(hands, key=hand_rank)

def rank_hand(hand):
    """return a value to represent the hand's absolute rank"""
    ranks = extract_ranks(hand)
    if is_straight(ranks) and is_flush(hand):
        return (8, max(ranks))
    elif is_of_kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    else:
        pass

def extract_ranks(hand):
    """return list of card ranks from hand, without the suit"""
    pass

def is_straight(card_ranks):
    """return True if card_ranks form a straight"""
    pass

def is_flush(hand):
    """return True if all items in hand are in the same suit"""
    pass

def is_of_kind(target_size, card_ranks):
    """return highest rank if hand contains target_size repeated rank 
    values within card_ranks, or False otherwise"""
    pass

def test():
    """test cases for poker program"""
    straight_flush = "6C 7C 8C 9C TC".split()
    four_kind = "9D 9H 9S 9C 7D".split()
    full_house = "TD TC TH 7C 7D".split()

    assert best_hand([straight_flush, four_kind, full_house]) == straight_flush
    assert best_hand([full_house, four_kind]) == four_kind
    assert best_hand([full_house, full_house]) == full_house
    assert best_hand([straight_flush]) == straight_flush
    assert best_hand([straight_flush for i in range(100)]) == straight_flush

    return True
