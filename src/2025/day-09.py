from itertools import combinations
from shapely.geometry import Polygon

with open("day-09.txt", "r") as f:
    input_data = f.read().strip().split("\n")

tiles = []
for line in input_data:
    x, y = map(int, line.split(","))
    tiles.append((x, y))

# Part 1

combos = combinations(tiles, 2)

areas = []
for tile1, tile2 in combos:
    area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
    areas.append(area)

ans = max(areas)
print(ans)


# Part 2

tiles.append(tiles[0])
outer_polygon = Polygon(tiles)

combos = combinations(tiles, 2)

areas = []
for tile1, tile2 in combos:
    tile3 = (tile2[0], tile1[1])
    tile4 = (tile1[0], tile2[1])
    corners = [tile1, tile3, tile2, tile4, tile1]
    inner_polygon = Polygon(corners)
    if outer_polygon.covers(inner_polygon):
        area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        areas.append(area)

ans = max(areas)
print(ans)
