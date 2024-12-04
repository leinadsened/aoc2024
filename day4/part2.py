import re

with open("day4/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

count = 0
patterns = ["MAS", "SAM"]

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == 'A':
            top_left = lines[i-1][j-1]
            top_right = lines[i-1][j+1]
            bottom_left = lines[i+1][j-1]
            bottom_right = lines[i+1][j+1]
            pattern1 = top_left + 'A' + bottom_right
            pattern2 = top_right + 'A' + bottom_left

            if pattern1 in patterns and pattern2 in patterns:
                count += 1

print(count)
