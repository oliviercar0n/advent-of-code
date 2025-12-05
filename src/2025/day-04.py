import numpy as np

with open("day-04.txt", "r") as f:
    input_data = f.read().strip().split("\n")


# Part 1

acc = 0
a = np.array([list(row) for row in input_data])

j, i = a.shape

acc = 0
for y in range(j):
    for x in range(i):
        if a[y][x] == "@":
            adj_rolls = 0
            for yo in range(-1, 2):
                for xo in range(-1, 2):
                    if not (yo == 0 and xo == 0):
                        new_y = y + yo
                        new_x = x + xo
                        if 0 <= new_y < j and 0 <= new_x < i:
                            if a[new_y][new_x] == "@":
                                adj_rolls += 1
            if adj_rolls < 4:
                acc += 1

print(acc)


# Part 2

removed = 1
next_m = a.copy()
acc = 0
while removed > 0:
    removed = 0
    current_m = next_m.copy()
    for y in range(j):
        for x in range(i):
            if current_m[y][x] == "@":
                adj_rolls = 0
                for yo in range(-1, 2):
                    for xo in range(-1, 2):
                        if not (yo == 0 and xo == 0):
                            new_y = y + yo
                            new_x = x + xo
                            if 0 <= new_y < j and 0 <= new_x < i:
                                if current_m[new_y][new_x] == "@":
                                    adj_rolls += 1
                if adj_rolls < 4:
                    removed += 1
                    next_m[y][x] = "."
    acc += removed
print(acc)
