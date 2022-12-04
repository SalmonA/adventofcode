with open('input.txt', 'r') as f:
    q1, q2 = 0, 0
    for line in f:
        e = list(map(int, line.replace('-', ',').split(",")))
        elf1, elf2 = set(range(e[0],e[1]+1)), set(range(e[2],e[3]+1))
        intersection = elf1.intersection(elf2)
        # Q1
        if len(intersection) == min(len(elf1), len(elf2)):
            q1 += 1
        #Q2
        if len(intersection):
            q2 += 1

print(q1)
print(q2)
