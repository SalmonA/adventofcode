with open('input.txt', 'r') as f:
    input = f.readlines()

priorities = 0

for groupIndex in range(len(input)//3):
    group = input[groupIndex*3:groupIndex*3+3]
    for c in group[0]:
        if c in group[1] and c in group[2]:
            print(c)
            priorities += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1
            break

print(priorities)

