from collections import Counter


with open("day-01.txt", "r") as f:
    input_data = f.read().strip().split("\n")

# Part 1

left = sorted(int(line.split("   ")[0].strip()) for line in input_data)
right = sorted(int(line.split("   ")[1].strip()) for line in input_data)

acc = sum(abs(left[i] - right[i]) for i in range(len(left)))

print(acc)

# Part 2

left_unique = list(set(left))
freq = Counter(right)

acc = sum(n * freq[n] for n in left_unique)

print(acc)
