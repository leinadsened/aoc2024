from itertools import product

sum = 0

def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        else:
            result = int(str(result) + str(numbers[i + 1]))
    return result

with open("day7/input.txt") as f:
    lines = f.readlines()
    
for line in lines:
    goal, numbers = line.split(":")
    goal = int(goal)
    numbers = list(map(int, numbers.strip().split(" ")))
    
    possible_operators = ['+', '*', 'concat']
    operator_positions = len(numbers) - 1
    found = False
    
    for ops in product(possible_operators, repeat=operator_positions):
        if evaluate(numbers, ops) == goal:
            sum += goal
            found = True
            break

print(sum)
