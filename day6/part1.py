def is_valid_position(pos, grid):
    return (0 <= pos[0] < len(grid) and 
            0 <= pos[1] < len(grid[0]))

grid = []
position = (0,0)
facing = ""

with open("day6/input.txt") as f:
    for index, line in enumerate(f.readlines()):
        if any(char in line for char in "^>v<"):
            for char in "^>v<":
                pos = line.find(char)
                if pos != -1:
                    position = (index, pos)
                    facing = char
        grid.append(list(line.strip()))

visited_coords = {position}
in_bounds = True

while in_bounds:
    next_pos = position
    if facing == "^":
        next_pos = (position[0] - 1, position[1])
    elif facing == "v":
        next_pos = (position[0] + 1, position[1])
    elif facing == "<":
        next_pos = (position[0], position[1] - 1)
    elif facing == ">":
        next_pos = (position[0], position[1] + 1)
    
    if not is_valid_position(next_pos, grid):
        break
    
    if grid[next_pos[0]][next_pos[1]] == "#":
        if facing == "^": facing = ">"
        elif facing == ">": facing = "v"
        elif facing == "v": facing = "<"
        elif facing == "<": facing = "^"
    else:
        position = next_pos
        visited_coords.add(position)

print(len(visited_coords))