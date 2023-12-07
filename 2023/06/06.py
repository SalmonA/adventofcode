import math

with open('input.txt', 'r') as f:
    # input = [map(int,line.split()[1:]) for line in f.readlines()] # Part 1
    input = [[int("".join(line.split()[1:]))] for line in f.readlines()]

total = 1
for time, distance in zip(input[0], input[1]):
    delta = math.sqrt(time ** 2 + (4 * -distance))
    r1, r2 = (time - delta) / 2, (time + delta) / 2
    total *= math.floor(r2 - 1e-10) - math.ceil(r1 + 1e-10) + 1
    
print(total)