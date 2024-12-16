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

def get_next_position(pos, direction):
    moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    dx, dy = moves[direction]
    return (pos[0] + dx, pos[1] + dy)

def find_optimal_paths(grid):
    start, end = find_start_end(grid)
    directions = ['^', '>', 'v', '<']
    optimal_tiles = set([start])
    min_cost = float('inf')
    
    # Track costs for each position
    costs = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    # Priority queue: (cost, position, direction)
    pq = [(0, start, '>', {start})]
    
    while pq:
        cost, pos, facing, path = heappop(pq)
        
        if pos == end:
            if cost <= min_cost:
                min_cost = cost
                optimal_tiles.update(path)
            continue
            
        # Allow equal cost paths
        if cost > costs[pos][facing] + 1000:
            continue
            
        for new_dir in directions:
            next_pos = get_next_position(pos, new_dir)
            if not is_valid_position(next_pos, grid):
                continue
                
            new_cost = cost
            if new_dir != facing:
                new_cost += 1000
            new_cost += 1
            
            if new_cost <= costs[next_pos][new_dir] + 1000:
                costs[next_pos][new_dir] = min(costs[next_pos][new_dir], new_cost)
                new_path = path | {next_pos}
                heappush(pq, (new_cost, next_pos, new_dir, new_path))
    
    return len(optimal_tiles)

def main():
    grid = parse_input('day16/input.txt')
    result = find_optimal_paths(grid)
    print(f"Number of tiles in optimal paths: {result}")

if __name__ == '__main__':
    main()
