with open('input.txt', 'r') as f:
    input = []
    for x in [line.strip().split(':')[1].split('|') for line in f.readlines()]:
        input += [[list(map(int,y.split())) for y in x]]

# Part 1
part1 = 0
for winning, actual in input:
    nb_winning = 0
    for number in winning:
        if number in actual: 
            nb_winning += 1
    if nb_winning: 
        part1 += 2 ** (nb_winning - 1)
    
print("Part 1:", part1)

# Part 2
counts = {}
for index, (winning, actual) in enumerate(input, 1):
    nb_winning = 0
    # Add original
    counts[index] = counts.get(index, 0) + 1
    for number in winning:
        if number in actual: 
            nb_winning += 1
    for value in range(index + 1, index + 1 + nb_winning):
        counts[value] = counts.get(value, 0) + counts.get(index, 0)
 
print("Part 2:", sum(counts.values()))