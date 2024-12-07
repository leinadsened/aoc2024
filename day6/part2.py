def is_valid_position(pos, grid):
    return (0 <= pos[0] < len(grid) and 
            0 <= pos[1] < len(grid[0]))

def simulate_path(grid, start_pos, start_facing, obstacle_pos):
    test_grid = [row[:] for row in grid]
    if obstacle_pos:
        test_grid[obstacle_pos[0]][obstacle_pos[1]] = "#"
    
    position = start_pos
    facing = start_facing
    visited_states = set()
    
    while True:
        current_state = (position, facing)

        if current_state in visited_states:
            return True
            
        visited_states.add(current_state)
        
        if facing == "^": next_pos = (position[0] - 1, position[1])
        elif facing == "v": next_pos = (position[0] + 1, position[1])
        elif facing == "<": next_pos = (position[0], position[1] - 1)
        elif facing == ">": next_pos = (position[0], position[1] + 1)
        
        if not is_valid_position(next_pos, test_grid):
            return False
            
        if test_grid[next_pos[0]][next_pos[1]] == "#":
            if facing == "^": facing = ">"
            elif facing == ">": facing = "v"
            elif facing == "v": facing = "<"
            elif facing == "<": facing = "^"
        else:
            position = next_pos

grid = []
start_pos = (0,0)
start_facing = ""

with open("day6/input.txt") as f:
    for index, line in enumerate(f.readlines()):
        if any(char in line for char in "^>v<"):
            for char in "^>v<":
                pos = line.find(char)
                if pos != -1:
                    start_pos = (index, pos)
                    start_facing = char
        grid.append(list(line.strip()))

valid_positions = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#" or (i, j) == start_pos:
            continue
            
        has_loop = simulate_path(grid, start_pos, start_facing, (i, j))
        if has_loop:
            valid_positions += 1

print(valid_positions)