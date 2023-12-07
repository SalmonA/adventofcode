with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()] 

# Part 1
part_numbers = []

def symbol_in_neighbours(x,y): 
    ignore = "1234567890."

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 <= x+i < len(input) and 0 <= y+j < len(input[0]):
                if input[x+i][y+j] not in ignore:
                    return True
    return False

for x, line in enumerate(input):
    numbers = []
    current_len = 0
    is_part_number = False
    for y, character in enumerate(line):
        if character.isnumeric():
            current_len +=1
            if symbol_in_neighbours(x,y):
                is_part_number = True
        else:
            if current_len > 0 and is_part_number:
                part_numbers.append(int(line[y-current_len:y]))
            current_len = 0
            is_part_number = False
        if y == len(line) - 1 :
            if current_len > 0 and is_part_number:
                part_numbers.append(int(line[y+1-current_len:y+1]))

print("Part 1:", sum(part_numbers))

# Part 2
gear_parts = {}

def gear_in_neighbours(x,y): 
    gears = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 <= x+i < len(input) and 0 <= y+j < len(input[0]):
                if input[x+i][y+j] == "*":
                    gears.append((x+i, y+j))
    return gears

for x, line in enumerate(input):
    numbers = []
    current_len = 0
    is_part_number = False
    neighbouringGear = []
    for y, character in enumerate(line):
        if character.isnumeric():
            current_len +=1
            if len(gear_in_neighbours(x,y)) > 0 :
                neighbouringGear = gear_in_neighbours(x,y)
                is_part_number = True    
        else:
            if current_len > 0 and is_part_number:
               for gear in neighbouringGear: 
                gear_parts[gear] = gear_parts.get(gear, []) + [int(line[y-current_len:y])]
            current_len = 0
            is_part_number = False
        if y == len(line) - 1 :
            if current_len > 0 and is_part_number:
               for gear in neighbouringGear: 
                gear_parts[gear] = gear_parts.get(gear, []) + [int(line[y+1-current_len:y+1])]

total = 0
for value in gear_parts.values():
    if len(value) == 2:
        total += value[0] * value[1] 
   
print("Part 2:", total)
    
