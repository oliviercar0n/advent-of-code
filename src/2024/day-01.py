import collections

with open("day-01.txt", "r") as f:
    input_data = f.read().strip().split("\n")

# Part 1

list_one = []
list_two = []
for line in input_data:
    list_one.append(int(line.split("   ")[0].strip()))
    list_two.append(int(line.split("   ")[1].strip()))

list_one = sorted(list_one)
list_two = sorted(list_two)

acc = 0
for i in range(len(list_one)):
    acc += abs(list_one[i] - list_two[i])

print(acc)

# Part 2

set_one = list(set(list_one))
counter = collections.Counter(list_two)

acc = 0
for i in set_one:
    acc += i * counter[i]

print(acc)