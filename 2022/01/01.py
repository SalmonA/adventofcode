with open('input.txt', 'r') as f:
    calories = []
    carriedCalories = 0
    for line in f:
        if line == "\n":
            calories.append(carriedCalories)
            carriedCalories = 0
        else:
            carriedCalories += int(line)

# Part 1
print(max(calories))
# Part 2
print(sum(sorted(calories, reverse=True)[:3]))
