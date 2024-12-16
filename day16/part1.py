
from heapq import heappush, heappop
from collections import defaultdict

def parse_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start_end(grid):
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def is_valid_position(pos, grid):
    return (0 <= pos[0] < len(grid) and 
            0 <= pos[1] < len(grid[0]) and 
            grid[pos[0]][pos[1]] != '#')

def get_direction_index(direction):
    return {'^': 0, '>': 1, 'v': 2, '<': 3}[direction]

def get_next_position(pos, direction):
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dx, dy = moves[direction]
    return (pos[0] + dx, pos[1] + dy)

def solve(grid):
    start, end = find_start_end(grid)
    directions = ['^', '>', 'v', '<']
    
    # Priority queue: (cost, position, direction)
    pq = [(0, start, '>')]
    visited = defaultdict(lambda: float('inf'))
    
    while pq:
        cost, pos, facing = heappop(pq)
        
        if pos == end:
            return cost
            
        state = (pos, facing)
        if cost >= visited[state]:
            continue
        visited[state] = cost
        
        # Try moving forward
        next_pos = get_next_position(pos, facing)
        if is_valid_position(next_pos, grid):
            heappush(pq, (cost + 1, next_pos, facing))
        
        # Try turning left and right
        current_dir_idx = get_direction_index(facing)
        for turn in [-1, 1]:  # -1 for left turn, 1 for right turn
            new_dir_idx = (current_dir_idx + turn) % 4
            new_dir = directions[new_dir_idx]
            heappush(pq, (cost + 1000, pos, new_dir))
    
    return float('inf')

def main():
    grid = parse_input('day16/input.txt')
    result = solve(grid)
    print(f"Minimum score required: {result}")

if __name__ == '__main__':
    main()
