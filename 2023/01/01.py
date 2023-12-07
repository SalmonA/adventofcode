with open('input.txt', 'r') as f:
    input = f.readlines()

part1 = 0
part2 = 0

for line in input:
    numbers = [int(x) for x in line if x.isnumeric()]
    part1 +=  numbers[0] * 10 + numbers[-1] 
    
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
           "six": 6, "seven": 7, "eight": 8, "nine": 9}

for line in input:
    digits = []
    for i in range(len(line)):
        for j in range(1, len(line)):
            if line[i:j].isnumeric():
                digits.append(int(line[i:j]))
            if line[i:j] in numbers: 
                digits.append(numbers[line[i:j]])
    part2 += digits[0] * 10 + digits[-1] 


print("Part 1:", part1)
print("Part 2:", part2)
