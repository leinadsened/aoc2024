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

sum = 0

for seq in sequences:
    if is_valid_sequence(seq, rules):
        middle_index = (len(seq) - 1) // 2
        sum += seq[middle_index]

print(sum)