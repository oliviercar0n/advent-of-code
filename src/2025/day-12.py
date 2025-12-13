with open("day-12.txt", "r") as f:
    input_data = f.read().strip().split("\n\n")


shapes = {}
regions = []
for part in input_data:
    lines = part.split("\n")
    if lines[0].endswith(":"):
        shapes[lines[0][0]] = [list(line) for line in lines[1:]]
    else:
        for line in part.split("\n"):
            dim, qnt = line.split(": ")
            width, length = map(int, dim.split("x"))
            qnt = map(int, qnt.split(" "))
            regions.append((width, length, qnt))

# Part 1

ans = len(
    [sum(qnt) for width, length, qnt in regions if sum(qnt) <= width // 3 * length // 3]
)

print(ans)
