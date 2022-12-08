with open('input.txt', 'r') as f:
    history = [line[:-1] for line in f.readlines()]

totalVisible = 0
scenicScores = []

def getScenicScore(x, y, list):
    score = 0
    for e in list: 
        score += 1
        if int(e) >= int(history[x][y]):
            break
    return score
    
for rowIndex in range(len(history)):
    for colIndex in range(len(history[0])):

        top = [x[colIndex] for x in history[:rowIndex]][::-1]
        bottom = [x[colIndex] for x in history[rowIndex+1:]]
        left = history[rowIndex][:colIndex][::-1]
        right = history[rowIndex][colIndex+1:]

        #Q1
        if any(
            [
            all([int(x) < int(history[rowIndex][colIndex]) for x in top]),
            all([int(x) < int(history[rowIndex][colIndex]) for x in bottom]),
            all([int(x) < int(history[rowIndex][colIndex]) for x in left]),
            all([int(x) < int(history[rowIndex][colIndex]) for x in right])]
        ):
            totalVisible += 1

        #Q2
        scenicScores.append(
            getScenicScore(rowIndex, colIndex, top) *
            getScenicScore(rowIndex, colIndex, bottom) *
            getScenicScore(rowIndex, colIndex, left) *
            getScenicScore(rowIndex, colIndex, right)
        )

print(totalVisible)
print(max(scenicScores))