import re


def mult_mul(my_string):
    mul_list = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", my_string)
    sum = 0
    for mul in mul_list:
        mul = mul.replace("mul(", "")
        mul = mul.replace(")", "")
        a, b = map(int, mul.split(","))
        sum += a*b
    return sum


with open("day3/input.txt") as f:
    input = f.read()
sum = 0
dos = re.split(r"do\(\)", input)
for item in dos:
    strings = re.split(r"don't\(\)", item)
    my_string = strings[0]
    sum += mult_mul(my_string)
print(sum)