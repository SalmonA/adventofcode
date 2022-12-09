with open('input.txt', 'r') as f:
    grid = [list(map(int, list(line[:-1]))) for line in f.readlines()]

totalVisible = 0
scenicScores = []

def getScenicScore(x, y, list):
    score = 0
    for e in list:
        score += 1
        if e >= grid[x][y]:
            break
    return score

for r in range(len(grid)):
    for c in range(len(grid[r])):

        top = [grid[x][c] for x in range(r)][::-1]
        bottom = [grid[x][c] for x in range(r+1, len(grid[r]))]
        left = [grid[r][x] for x in range(c)][::-1]
        right = [grid[r][x] for x in range(c+1, len(grid[r]))]

        # Q1
        if any(
            [
                all([x < grid[r][c] for x in top]),
                all([x < grid[r][c] for x in bottom]),
                all([x < grid[r][c] for x in left]),
                all([x < grid[r][c] for x in right])]
        ):
            totalVisible += 1

        # Q2
        scenicScores.append(
            getScenicScore(r, c, top) *
            getScenicScore(r, c, bottom) *
            getScenicScore(r, c, left) *
            getScenicScore(r, c, right)
        )

print(totalVisible)
print(max(scenicScores))
