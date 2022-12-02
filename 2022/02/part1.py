score = 0

with open('input.txt', 'r') as f:
    gap = ord('A') - ord('X')
    for line in f:
        p1, p2 = line[:-1].split(' ')
        result = (ord(p1) - ord(p2) - gap) % 3
        if result == 0:
            score += 3
        elif result == 2:
            score += 6
        score += "XYZ".index(p2)+1

print(score)