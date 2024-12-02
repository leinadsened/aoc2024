def check_level(line):
    if line[0] - line[1] > 0:
        for i in range(len(line) - 1):
            num = line[i] - line[i+1]
            if num <= 0 or abs(num) > 3:
                break
            if i == len(line) - 2:
                return True
    elif line[0] - line[1] < 0:
        for i in range(len(line) - 1):
            num = line[i + 1] - line[i]
            if num <= 0 or abs(num) > 3:
                break
            if i == len(line) - 2:
                return True
    return False

def modified_levels(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if check_level(modified_levels):
            return True
    return False


# Read input and process lines
with open("day2/input.txt") as f:
    lines = [list(map(int, line.strip().split())) for line in f]

safe = 0
for line in lines:
    if modified_levels(line):
        safe += 1

print(safe)
