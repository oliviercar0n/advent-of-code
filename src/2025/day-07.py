import numpy as np


with open("day-07.txt", "r") as f:
    input_data = f.read().strip().split("\n")

# Part 1

m = np.array([list(row) for row in input_data])
j, i = m.shape

start_x, start_y = np.where(m == "S")
start_pos = (int(start_x[0]), int(start_y[0]))

next_beams = []
next_beams.append(start_pos)

ans = 0
for row in range(j - 1):
    current_beams = next_beams.copy()
    next_beams = []
    for i, beam in enumerate(current_beams):
        new_pos = (beam[0] + 1, beam[1])
        pos_value = m[new_pos[0]][new_pos[1]]
        if pos_value == "^":
            ans += 1
            new_pos_split = (new_pos[0], new_pos[1] + 1)
            if new_pos_split not in next_beams:
                next_beams.append(new_pos_split)
            new_pos = (new_pos[0], new_pos[1] - 1)
            if new_pos not in next_beams:
                next_beams.append(new_pos)
        else:
            if new_pos not in next_beams:
                next_beams.append(new_pos)

print(ans)


# Part 2

next_beams = {start_pos: 1}

ans = 0
for row in range(j - 1):
    current_beams = next_beams.copy()
    next_beams = {}
    for pos, count in current_beams.items():
        new_pos = (pos[0] + 1, pos[1])
        pos_value = m[new_pos[0]][new_pos[1]]
        if pos_value == "^":
            new_pos_split = (new_pos[0], new_pos[1] + 1)
            if new_pos_split not in next_beams.keys():
                next_beams[new_pos_split] = count
            else:
                next_beams[new_pos_split] += count
            new_pos = (new_pos[0], new_pos[1] - 1)
            if new_pos not in next_beams.keys():
                next_beams[new_pos] = count
            else:
                next_beams[new_pos] += count
        else:
            if new_pos not in next_beams.keys():
                next_beams[new_pos] = count
            else:
                next_beams[new_pos] += count


ans = sum(next_beams.values())
print(ans)
