with open('input.txt', 'r') as f:
    score = 0
    for line in f:
        p1, p2 = line.split()
        # Cycle, winning move is at n-1, draw at n, and lose at n+1
        score += (("ABC".index(p1) + "XYZ".index(p2)-1) % 3) + 1
        score += ("XYZ".index(p2)) * 3

print(score)

