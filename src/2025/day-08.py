import math
from itertools import combinations

with open("day-08.txt", "r") as f:
    input_data = f.read().strip().split("\n")


def connect_circuits(box1, box2, n_circuits):
    for circuit in n_circuits:
        if box1 in circuit:
            box1_circuit = circuit
        if box2 in circuit:
            box2_circuit = circuit

    if box1_circuit != box2_circuit:
        n_circuits.remove(box1_circuit)
        n_circuits.remove(box2_circuit)
        box1_circuit.extend(box2_circuit)
        n_circuits.append(box1_circuit)

    return n_circuits


boxes = []
for line in input_data:
    x, y, z = map(int, line.split(","))
    boxes.append((x, y, z))

combos = combinations(boxes, 2)

combos_distances = []
for box1, box2 in combos:
    combos_distances.append((box1, box2, math.dist(box1, box2)))

sorted_combos = sorted(combos_distances, key=lambda x: x[2])

n_circuits = []
for box in boxes:
    n_circuits.append([box])

# Part 1

for box1, box2, distance in sorted_combos[:1000]:
    circuits = n_circuits.copy()
    n_circuits = connect_circuits(box1, box2, n_circuits)

circuit_len = [len(circuit) for circuit in n_circuits]
circuit_len_sorted = sorted(circuit_len, reverse=True)

ans = math.prod(circuit_len_sorted[:3])

print(ans)


# Part 2

for box1, box2, distance in sorted_combos:
    circuits = n_circuits.copy()
    n_circuits = connect_circuits(box1, box2, n_circuits)

    if len(n_circuits) == 1:
        ans = box1[0] * box2[0]
        break

print(ans)
