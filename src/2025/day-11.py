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

ans = dfs(graph, "you", "out", {})
print(ans)


# Part 2

memo = {}
ans = (
    dfs(graph, "svr", "fft", {})
    * dfs(graph, "fft", "dac", {})
    * dfs(graph, "dac", "out", {})
)
print(ans)
