with open("day-01.txt", "r") as f:
    input_data = f.read().strip().split("\n")

# Part 1

pos = 50
acc = 0
for ins in input_data:
    d = ins[0]
    i = int(ins[1:])

    i = i % 100

    if d == "L":
        pos -= i
    elif d == "R":
        pos += i

    if pos >= 100:
        pos -= 100
    elif pos < 0:
        pos += 100

    if pos == 0:
        acc += 1

print(acc)


# Part 2

pos = 50
acc = 0
for ins in input_data:
    d = ins[0]
    i = int(ins[1:])

    if d == "L":
        inc = -1
    else:
        inc = 1

    for _ in range(i):
        pos += inc

        if pos >= 100:
            pos -= 100
        elif pos < 0:
            pos += 100

        if pos == 0:
            acc += 1

print(acc)
