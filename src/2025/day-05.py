from itertools import combinations

with open("day-05.txt", "r") as f:
    input_data = f.read().strip()

ranges, ingredients = input_data.split("\n\n")

# Part 1

acc = 0
for id in ingredients.split("\n"):
    id = int(id)
    for r in ranges.split("\n"):
        lbound, ubound = r.split("-")
        lbound = int(lbound)
        ubound = int(ubound)
        if lbound <= id <= ubound:
            acc += 1
            break

print(acc)


# Part 2

rl = ranges.split("\n")

intervals = []
for r in rl:
    lbound, ubound = r.split("-")
    lbound = int(lbound)
    ubound = int(ubound)
    intervals.append((lbound, ubound))

intervals.sort(key=lambda x: x[0])

merged = []
cur_start, cur_end = intervals[0]
for next_start, next_end in intervals[1:]:
    if next_start <= cur_end:
        cur_end = max(cur_end, next_end)
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = next_start, next_end

merged.append((cur_start, cur_end))

acc = 0
for start, end in merged:
    acc += end - start + 1

print(acc)
