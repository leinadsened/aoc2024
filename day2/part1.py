with open("day2/input.txt") as f:
    lines = f.readlines()
safe = 0
for line in lines:
    line = line.strip().split(" ")
    if int(line[0]) - int(line[1]) > 0:
        for i in range(len(line) - 1):
            num = int(line[i]) - int(line[i+1])
            if num <= 0 or abs(num) > 3:
                break
            if i == len(line) - 2:
                safe += 1
    elif int(line[0]) - int(line[1]) < 0:
        for i in range(len(line) - 1):
            num = int(line[i + 1]) - int(line[i])
            if num <= 0 or abs(num) > 3:
                break
            if i == len(line) - 2:
                safe += 1

print(safe)