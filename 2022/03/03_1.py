with open('input.txt', 'r') as f:
    priorities = 0
    for line in f:
        l = len(line)//2
        s1, s2 = line[l:-1], line[:l]
        for c in s1:
            if c in s2:
                priorities += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1
                break

print(priorities)

