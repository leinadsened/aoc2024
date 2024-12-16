def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def move_boxes(grid, position, next_position):
    direction_row = next_position[0] - position[0]
    direction_col = next_position[1] - position[1]
    print(direction_row, direction_col)
    current_box_position = next_position
    while True:
        box_next_row = current_box_position[0] + direction_row
        box_next_col = current_box_position[1] + direction_col
        box_next_position = (box_next_row, box_next_col)
        if grid[box_next_row][box_next_col] == "#":
            return position

        if grid[box_next_row][box_next_col] == ".":
            grid[box_next_row][box_next_col] = "O"
            while current_box_position != next_position:
                box_next_row -= direction_row
                box_next_col -= direction_col
                current_box_position = (box_next_row, box_next_col)
                grid[box_next_row][box_next_col] = "O"
            grid[next_position[0]][next_position[1]] = "@"
            grid[position[0]][position[1]] = "."
            return next_position

        current_box_position = box_next_position

def move_to(grid, position, direction):
    if direction == "^":
        next_position = (position[0]-1, position[1])
    elif direction == "v":
        next_position = (position[0]+1, position[1])
    elif direction == "<":
        next_position = (position[0], position[1]-1)
    elif direction == ">":
        next_position = (position[0], position[1]+1)
    print(grid[next_position[0]][next_position[1]])
    if grid[next_position[0]][next_position[1]] == "#":
        return position
    elif grid[next_position[0]][next_position[1]] == "O":
        new_position = move_boxes(grid, position, next_position)
        return new_position
    else:
        grid[next_position[0]][next_position[1]] = "@"
        grid[position[0]][position[1]] = "."
        return next_position


with open("day15/input.txt", "r") as f:
    lines = f.readlines()
print(lines)
position = (0,0)
grid = []
moves = ""
for line in lines:
    if line[0] == "#":
        grid.append(list(line.strip()))
        if "@" in line:
            position = (len(grid) - 1, line.index("@"))
    else:
        moves += line.strip()
next_position = position
for move in moves:
    next_position = move_to(grid, next_position, move)
    print(f"Move: {move}")
    print_grid(grid)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            total += (100 * i + j)
print(total)