import re

with open("day4/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
count = 0
for line in lines:
    matches = re.findall("XMAS", line)
    matches_backwards = re.findall("SAMX", line)
    count += len(matches) + len(matches_backwards)

rows = [''.join(row) for row in zip(*lines)]
for row in rows:
    matches = re.findall("XMAS", row)
    matches_backwards = re.findall("SAMX", row)
    count += len(matches) + len(matches_backwards)

def get_diagonals(grid):
    diagonals = []
    n, m = len(grid), len(grid[0])
    for d in range(n + m - 1):
        diag1 = []
        diag2 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(grid[i][d - i])
            diag2.append(grid[i][m - 1 - (d - i)])
        if diag1:
            diagonals.append(''.join(diag1))
        if diag2:
            diagonals.append(''.join(diag2))
    return diagonals

grid = [list(line) for line in lines]
diagonals = get_diagonals(grid)

for diag in diagonals:
    matches = re.findall("XMAS", diag)
    matches_backwards = re.findall("SAMX", diag)
    count += len(matches) + len(matches_backwards)

print(count)