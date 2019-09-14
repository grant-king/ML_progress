# design and implement and elementary greedy algorithm to find the
# minimum number of coins needed to change the input integer value 
# into coins with denominations of 1, 5, and 10

def get_change(change):
    COIN_VALUES = sorted([1, 5, 10], reverse=True)
    coin_counts = {str(value): 0 for value in COIN_VALUES}

    for coin_value in COIN_VALUES:
        coin_counts[str(coin_value)] = change // coin_value
        change = change % coin_value

    min_coins = sum(coin_counts.values())
    return min_coins


