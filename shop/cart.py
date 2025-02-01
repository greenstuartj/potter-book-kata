from collections import Counter, namedtuple

def price(items):
    """
    price algorithm
    
    if the basket is empty, price is 0

    find the most common item in the basket and create n discount groups
      where n in the number of times the most common item appears in the basket

    for all remaining items in the basket after the most common item
      check which discount groups the item can be added to
      of those groups, find the group which would have the largest drop in discount
        when the discount drops are equal, prioritise the first group
      add the item to that group

    price is the sum of base price, multiplied by group size, multiplied by discount, for each group

    NOTE:
      discounts are stored as integers, as finding the largest drop in discount would otherwise compare
        floating point numbers, and the imprecision can prioritse the incorrect discount group when the
        integer representations should be equal
    """
    
    base_price = 8
    discounts  = { 1: 100, 2: 95, 3: 90, 4: 80, 5: 75 }
    
    if len(items) == 0:
        return 0
    
    counts           = Counter(items)
    sorted_items     = sorted(items, key = lambda item: counts[item], reverse = True)
    most_common_item = sorted_items[0]
    group_n          = counts[most_common_item]
    groups           = [ set([most_common_item]) for _ in range(group_n) ]

    DiscountDrop = namedtuple('DiscountDrop', ['index', 'delta'])
    
    for item in sorted_items[group_n:]:
        new_discounts = []
        for i, group in enumerate(groups):
            if item not in group:
                new_discounts.append(DiscountDrop(i, discounts[len(group)] - discounts[len(group)+1]))
        sorted_discount_deltas = sorted(new_discounts, key = lambda p: p.delta, reverse = True)
        groups[sorted_discount_deltas[0].index].add(item)
        
    return sum([ base_price * len(g) * (discounts[len(g)] / 100) for g in groups ])
