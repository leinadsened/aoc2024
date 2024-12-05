rules = []
sequences = []

with open("day5/input.txt") as f:
    for line in f.readlines():
        if "|" in line:
            a_rule, b_rule = line.strip().split("|")
            rules.append((int(a_rule), int(b_rule)))
        elif "," in line:
            sequences.append(list(map(int, line.strip().split(","))))

def is_valid_sequence(seq, rules):
    for a, b in rules:
        if a in seq and b in seq:
            if seq.index(a) > seq.index(b):
                return False
    return True

def topological_sort(seq, rules):
    graph = {node: [] for node in seq}
    in_degree = {node: 0 for node in seq}

    for a, b in rules:
        if a in seq and b in seq:
            graph[a].append(b)
            in_degree[b] += 1

    queue = [node for node in seq if in_degree[node] == 0]
    sorted_seq = []

    while queue:
        node = queue.pop(0)
        sorted_seq.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_seq

sum = 0

for seq in sequences:
    if not is_valid_sequence(seq, rules):
        reordered_seq = topological_sort(seq, rules)
        middle_index = (len(reordered_seq) - 1) // 2
        sum += reordered_seq[middle_index]

print(sum)
