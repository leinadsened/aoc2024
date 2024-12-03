import re

with open("day3/input.txt") as f:
    my_string = f.read()
mul_list = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", my_string)
sum = 0
for mul in mul_list:
    mul = mul.replace("mul(", "")
    mul = mul.replace(")", "")
    
    a, b = map(int, mul.split(","))
    sum += a*b
print(sum)