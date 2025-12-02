from itertools import batched
import math

with open("day-02.txt", "r") as f:
    input_data = f.read().strip().split(",")


# Part 1

acc = 0
for rng in input_data:
    lbound = int(rng.split("-")[0])
    ubound = int(rng.split("-")[1])
    for id in range(lbound, ubound + 1):
        str_id = str(id)
        l = int(len(str_id) / 2)
        left = str_id[:l]
        right = str_id[l:]
        if left == right:
            acc += id

print(acc)


# Part 2

acc = 0
for rng in input_data:
    lbound = int(rng.split("-")[0])
    ubound = int(rng.split("-")[1])
    for id in range(lbound, ubound + 1):
        str_id = str(id)
        max_chunk = int(len(str_id)/2)
        for i in range(1, max_chunk + 1):
            split_list = list(batched(str_id, i))
            if len(set(split_list)) == 1:
                acc += id
                break

print(acc)
