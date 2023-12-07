with open('input.txt', 'r') as f:
    input = f.readlines()

maximums = {'red': 12, 'green' : 13, 'blue': 14}

total = 0 

for index, line in enumerate(input, 1):
    possible = True
    currentMax = {}

    sets = [x.strip().split(',') for x in line.split(':')[1].split(';')]
    items = [[item.strip().split(' ') for item in round] for round in sets]

    for item in items: 
        for quantity, color in item:
            if currentMax.get(color, 0) < int(quantity):
                currentMax[color] = int(quantity)

    # Part 1
    # for key, value in maximums.items():
    #     if current[key] > value:
    #         possible = False
    # if possible: 
    #     total += index

    power = 1
    for quantity in currentMax.values():
        power *= quantity

    total += power

        
        
print(total)
