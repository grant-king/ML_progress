# determine maximal value of fractions of items that fit into the knapsack

def maximum_loot_value(sack_weight_capacity, items_list):
    #items in list are tuple of value, weight
    knapsack = []
    knapsack_weight = 0
    room_left = sack_weight_capacity
    value_densities = [item[0] / item[1] for item in items_list]

    while room_left > 0:    
        densest_idx = value_densities.index(max(value_densities))
        value_densities.remove(max(value_densities))
        most_valuable = items_list.pop(densest_idx)

        #fracture most valuable if not enough room for it
        if most_valuable[1] > room_left:
            fraction = room_left / most_valuable[1]
            most_valuable = list(map(lambda x: x * fraction, most_valuable)) 

        knapsack.append(most_valuable)
        knapsack_weight += most_valuable[1]

        room_left = sack_weight_capacity - knapsack_weight
    
    return sum([item[0] for item in knapsack])

items = [
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4]
]

