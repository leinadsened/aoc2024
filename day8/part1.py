grid = []
antennas = set()
with open("day8/input.txt") as f:
    for line in f.readlines():
        chars = list(line.strip())
        for char in chars:
            if char != ".":
                antennas.add(char)
        grid.append(chars)
antinode_positions = set()
for antenna in antennas:
    antenna_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == antenna:
                antenna_positions.append((i, j))
    for i in range(len(antenna_positions)):
        current_antenna = antenna_positions[i]
        for j in range(i + 1, len(antenna_positions)):
            a = antenna_positions[i]
            b = antenna_positions[j]
            dx = b[1] - a[1]
            dy = b[0] - a[0]
            antinode1 = (b[0] + dy, b[1] + dx)
            antinode2 = (a[0] - dy, a[1] - dx)
            
            antinode_positions.add(antinode1)
            antinode_positions.add(antinode2)
count = 0
for pos in antinode_positions:
    if pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0]):
        count += 1
print(count)