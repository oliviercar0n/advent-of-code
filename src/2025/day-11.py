with open("day-11.txt", "r") as f:
    input_data = f.read().strip().split("\n")


graph = {}
for line in input_data:
    device, connections = line.split(":")
    connections = connections.strip().split(" ")
    graph[device] = connections


def dfs(graph, current, target, memo) -> int:
    if current == target:
        return 1

    key = current + target
    if key in memo:
        return memo[key]

    total = 0
    for neighbour in graph.get(current, []):
        total += dfs(graph, neighbour, target, memo)

    memo[key] = total
    return total


# Part 1

memo = {}
ans = dfs(graph, "you", "out", memo)

print(ans)


# Part 2

memo = {}
ans = (
    dfs(graph, "svr", "fft", memo)
    * dfs(graph, "fft", "dac", memo)
    * dfs(graph, "dac", "out", memo)
)

print(ans)
