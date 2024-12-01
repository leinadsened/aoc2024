with open("input.txt") as f:
    lines = f.readlines()
list_a = []
list_b = []
for line in lines:
    a, b = line.split('   ')
    list_a.append(a)
    list_b.append(b)
list_a.sort()
list_b.sort()
sum = 0
for i in range(len(list_a)):
    sum += abs(int(list_a[i]) - int(list_b[i]))
print(sum)