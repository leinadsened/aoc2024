def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

grid = []
antennas = {} 

with open("day8/input.txt") as f:
    for i, line in enumerate(f.readlines()):
        chars = list(line.strip())
        for j, char in enumerate(chars):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
        grid.append(chars)

antinode_positions = set()

for antenna_type, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            antinode_positions.add(positions[i])
            antinode_positions.add(positions[j])
            
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if is_collinear(positions[i], positions[j], (x, y)):
                        antinode_positions.add((x, y))

count = sum(1 for pos in antinode_positions 
           if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]))
print(count)