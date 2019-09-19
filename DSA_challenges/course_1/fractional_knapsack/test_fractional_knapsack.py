from fractional_knapsack import maximum_loot_value

def test_max_loot_value():
    #items should be tuple of value, weight
    items = [
        [20, 4],
        [18, 3],
        [14, 2]
    ]

    max_value = maximum_loot_value(7, items)

    assert max_value == 42
