import re

with open("day-03.txt", "r") as f:
    input_data = f.read().strip()

# Part 1

pattern = r"mul(\(\d+,\d+\))"
results = re.findall(pattern, input_data)

acc = 0
for mul in results:
    l, r = mul[1:-1].split(",")
    acc += int(l) * int(r)

print(acc)

# Part 2

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
results = re.findall(pattern, input_data)

acc = 0
do = True
for match in results:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif match.startswith("mul") and do:
        l, r = match[4:-1].split(",")
        acc += int(l) * int(r)

print(acc)
