with open("day-03.txt", "r") as f:
    input_data = f.read().strip().split("\n")

# Part 1

acc = 0
for bank in input_data:
    lb = [int(x) for x in bank]

    start = max(lb[:-1])
    start_pos = lb.index(start)
    end = max(lb[start_pos + 1 :])

    joltage = int(str(start) + str(end))
    acc += joltage

print(acc)

# Part 2

N_BATT = 12

acc = 0
for bank in input_data:
    l = [int(x) for x in bank]
    batt = []
    nl = l
    for i in range(N_BATT):
        rm = N_BATT - i - 1
        if rm > 0:
            lookup = nl[:-rm]
        else:
            lookup = nl
        digit = max(lookup)
        batt.append(digit)
        nl = nl[nl.index(digit) + 1 :]

    joltage = int("".join([str(x) for x in batt]))
    acc += joltage

print(acc)
