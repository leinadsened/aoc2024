with open("input.txt") as f:
    lines = f.readlines()
list_a = []
list_b = []
for line in lines:
    a, b = line.split('   ')
    list_a.append(a)
    list_b.append(b.strip())
similarity_score = 0
for item in list_a:
    similarity_score += int(item) * list_b.count(item)
print(similarity_score)