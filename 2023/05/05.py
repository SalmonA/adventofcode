with open('input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]
    seeds = [int(x) for x in input[0].split(': ')[1].split()]
    maps = {}
    current_map = None
    for line in input[2:]:
        if 'to' in line:
            current_map = line.split()[0]
        elif line == '':
            continue
        else: 
            maps[current_map] = maps.get(current_map, []) + [[int(x) for x in line.split()]]

# Part 1
min_location = 99999999999999999999

def mapValue(value, mappings): 
    for destination, source, length in mappings:
        if source <= value <= source + length: 
            return destination + (value - source)
    return value

for seed in seeds: 
    current_value = seed
    for map_name, mappings in maps.items():
        current_value = mapValue(current_value, mappings)
    if current_value < min_location:
        min_location = current_value
    
print(min_location)


# Part 2

def unmapValue(value, mappings): 
    for source, destination, length in mappings:
        if source <= value < source + length: 
            return destination + (value - source)
    return value

seed_ranges = [[seeds[x], seeds[x] + seeds[x+1]] for x in range(0, len(seeds), 2)]

reversed_maps = list(maps.items())[::-1]
location = 0
found = False
while True:
        if location % 100000 == 0:
            print('step:', location )
        current_value = location 
        for map_name, mappings in reversed_maps:
            current_value = unmapValue(current_value, mappings)
        for lower, upper in seed_ranges:
            if lower <= current_value <= upper:
                found = True
                break 
        if found:
            print(f'FOUND: location: {location}, seed: {current_value}')
            break
        location += 1








