with open('input.txt', 'r') as f:
    input = [line.split() for line in f.readlines()]

# card_order = "23456789TJQKA" # part 1
card_order = "J23456789TQKA" 

hand_types = [[5], [4], [3, 2], [3], [2, 2], [2], [1]] 

def get_hand_type_strength(hand):
    card_counts = {}
    for card in hand: 
        card_counts[card] = card_counts.get(card, 0) + 1
    jokers = card_counts.pop("J", 0)
    counts = sorted(list(card_counts.values()), reverse=True)
    for index, type in enumerate(hand_types):
        # if counts[:len(type)] == type: # Part 1
        if sum(counts[:len(type)]) + jokers == sum(type):
            return len(hand_types) - index
    return -1    
    
input.sort(key=lambda x: (
    get_hand_type_strength(x[0]), 
    [card_order.index(card) for card in x[0]])
    )

total = 0
for rank, (hand, bid) in enumerate(input, 1):
    total += rank * int(bid)

print(total)