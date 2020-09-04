"""Write a program to compare poker hands"""

def best_hand(hands):
    """return the best hand from hands hand list"""
    return max(hands, key=rank_hand)

def rank_hand(hand):
    """return a value to represent the hand's absolute rank"""
    ranks = extract_ranks(hand)
    if is_straight(ranks) and is_flush(hand):
        return (8, max(ranks))
    elif is_of_kind(4, ranks):
        return (7, is_of_kind(4, ranks), is_of_kind(1, ranks))
    elif is_of_kind(3, ranks) and is_of_kind(2, ranks):
        return (6, is_of_kind(3, ranks), is_of_kind(2, ranks))
    elif is_flush(hand):
        return (5, *is_flush(hand))
    elif is_straight(ranks):
        return (5, *is_straight(ranks))
    else:
        pass

def extract_ranks(hand):
    """return sorted list of card ranks as ints from hand, without the suit"""
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
    return sorted(map(int, ranks))

def is_straight(card_ranks):
    """return descending ordered ranks if card_ranks form a straight, or False otherwise"""
    for idx, card_rank in enumerate(card_ranks[:-1]):
        if card_rank + 1 == card_ranks[idx + 1]:
            pass
        else:
            return False

    return card_ranks[::-1]

def is_flush(hand):
    """return descending ranks if all items in hand are in the same suit"""
    suit = hand[0][1]
    flush_counter = 1
    for card in hand[1:]:
        if card[1] == suit:
            flush_counter += 1
    if flush_counter == 5:
        return extract_ranks(hand)[::-1]
    else:
        return False

def is_of_kind(target_size, card_ranks):
    """return rank of like cards if hand contains target_size repeated rank 
    values within card_ranks, or False otherwise"""
    for card_rank in card_ranks:
        if card_ranks.count(card_rank) == target_size:
            return card_rank

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
    assert rank_hand(straight_flush) == (8, 10)
    assert rank_hand(four_kind) == (7, 9, 7)
    assert rank_hand(full_house) == (6, 10, 7)

    print('All tests passed.')

test()
