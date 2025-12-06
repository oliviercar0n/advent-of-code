import re
import math

with open("day-06.txt", "r") as f:
    input_data = f.read().strip()


# Part 1

number_lists = []
for line in input_data.split("\n")[:-1]:
    numbers = re.split(r"\s+", line)
    numbers = [int(n) for n in numbers if n]
    number_lists.append(numbers)

ops = input_data.split("\n")[-1]
ops_list = re.split(r"\s+", ops)

acc = 0
for i in range(len(ops_list)):
    items = [nl[i] for nl in number_lists]
    if ops_list[i] == "+":
        acc += sum(items)
    elif ops_list[i] == "*":
        acc += math.prod(items)

print(acc)


# Part 2

number_lists = []
for line in input_data.split("\n")[:-1]:
    numbers = [n for n in line]
    number_lists.append(numbers)

# Pad the end of the lists so they are all the same length and add an extra space
max_len = max(len(nl) for nl in number_lists)
for nl in number_lists:
    while len(nl) < max_len + 1:
        nl.append(" ")

ops = input_data.split("\n")[-1]
ops_list = re.split(r"\s+", ops)

numbers = []
op_index = 0
acc = 0
for i in range(len(number_lists[3])):
    item = [number_lists[j][i] for j in range(len(number_lists))]
    if all(n == " " for n in item):
        if ops_list[op_index] == "+":
            acc += sum(numbers)
        elif ops_list[op_index] == "*":
            acc += math.prod(numbers)
        op_index += 1
        numbers = []
    else:
        num = int("".join(item))
        numbers.append(num)

print(acc)
