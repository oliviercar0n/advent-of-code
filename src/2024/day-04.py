import numpy as np

with open("day-04.txt", "r") as f:
    input_data = f.read().strip()

m = np.array([list(row) for row in input_data.split("\n")])

LEN = m.shape[1] - 3
LX = m.shape[1] - 2

acc = 0
for j in range(0, m.shape[1]):
    for i in range(0, m.shape[0]):
        # DOWN
        if list(m[j : j + 4, i]) == ["X", "M", "A", "S"]:
            acc += 1
        # UP
        if list(m[j - 3 : j + 1, i]) == ["S", "A", "M", "X"]:
            print("YUS", j, i)
            acc += 1
        # # LEFT
        if list(m[j, i - 3 : i + 1]) == ["S", "A", "M", "X"]:
            acc += 1
        # # RIGHT
        if list(m[j, i : i + 4]) == ["X", "M", "A", "S"]:
            acc += 1

        # # UP-LEFT
        if j > 2 and i > 2:
            if [str(m[j - k][i - k]) for k in range(4)] == ["X", "M", "A", "S"]:
                acc += 1

        # # UP-RIGHT
        if j > 2 and i < LEN:
            if [str(m[j - k][i + k]) for k in range(4)] == ["X", "M", "A", "S"]:
                acc += 1

        # # DOWN-LEFT
        if j < LEN and i > 2:
            if [str(m[j + k][i - k]) for k in range(4)] == ["X", "M", "A", "S"]:
                acc += 1

        # # DOWN-RIGHT
        if j < LEN and i < LEN:
            if [str(m[j + k][i + k]) for k in range(4)] == ["X", "M", "A", "S"]:
                acc += 1

print(acc)

# Part 2

acc = 0
for j in range(0, m.shape[1]):
    for i in range(0, m.shape[0]):
        #  M M
        #   A
        #  S S
        if j < LX and i < LX:
            if (
                m[j][i] == "M"
                and m[j][i + 2] == "M"
                and m[j + 1][i + 1] == "A"
                and m[j + 2][i] == "S"
                and m[j + 2][i + 2] == "S"
            ):
                acc += 1

        #  M S
        #   A
        #  M S
        if j < LX and i < LX:
            if (
                m[j][i] == "M"
                and m[j][i + 2] == "S"
                and m[j + 1][i + 1] == "A"
                and m[j + 2][i] == "M"
                and m[j + 2][i + 2] == "S"
            ):
                acc += 1

        #  S S
        #   A
        #  M M
        if j < LX and i < LX:
            if (
                m[j][i] == "S"
                and m[j][i + 2] == "S"
                and m[j + 1][i + 1] == "A"
                and m[j + 2][i] == "M"
                and m[j + 2][i + 2] == "M"
            ):
                acc += 1

        #  S M
        #   A
        #  S M
        if j < LX and i < LX:
            if (
                m[j][i] == "S"
                and m[j][i + 2] == "M"
                and m[j + 1][i + 1] == "A"
                and m[j + 2][i] == "S"
                and m[j + 2][i + 2] == "M"
            ):
                acc += 1



print(acc)
