# TODO: add start position parser

stacks = list(map(list, 
    ["FDBZTJRN", 
    "RSNJH", 
    "CRNJGZFQ",
    "FVNGRTQ",
    "LTQF",
    "QCWZBRGN",
    "FCLSNHM",
    "DNQMTJ",
    "PGS"]))

## Part 1
# with open('input.txt', 'r') as f:
#     for line in f:
#         q, origin, dest = [int(x) for i, x in enumerate(line.split(' ')) if i in [1,3,5] ]
#         for i in range(q):
#             stacks[dest-1].append(stacks[origin-1].pop())

## Part 2       
with open('input.txt', 'r') as f:
    for line in f:
        q, origin, dest = [int(x) for i, x in enumerate(line.split(' ')) if i in [1,3,5] ]
        carried = stacks[origin-1][-q:]
        stacks[origin-1] = stacks[origin-1][:-q]
        stacks[dest-1] += carried
        
       
print("".join([x[-1] for x in stacks]))
