from collections import defaultdict
import numpy as np
f = open('input.txt').read().strip().split("\n\n")
# f = open('small_input.txt').read().strip().split("\n\n")


class Tile:
    def __init__(self, id, grid):
        self.id = id
        # trbl
        self.edges = [
            grid[0],
            "".join([x[-1] for x in grid]),
            grid[-1],
            "".join([x[0] for x in grid])
        ]
        self.o = 0

# def get_edges(grid):
#     top = grid[0]
#     bottom = grid[-1]
#     left = [x[0] for x in grid]
#     right = [x[-1] for x in grid]

tiles = []
tilemap = {}
for paragraph in f:
    lines = paragraph.split("\n")
    name = int(lines[0].split(" ")[1][:-1])
    rest = lines[1:]
    # print(name, rest)
    thisTile = Tile(name, rest)
    tiles.append(Tile(name, rest))
    tilemap[name] = thisTile

# for tile in tiles:
    # print(tile.id, tile.edges)

a = defaultdict(int)
tile_lookup = defaultdict(list)
edge_lookup = defaultdict(list)
for tile in tiles:
    for edge in tile.edges:
        edge_lookup[tile.id].append(edge)
        rev_edge = edge[::-1]
        a[edge] += 1
        a[rev_edge] += 1
        tile_lookup[edge].append(tile.id)
        tile_lookup[rev_edge].append(tile.id)
c = 0    
# for edge in a.keys():
    
    # if a[edge] == 1:
    #     print(tile_lookup[edge])
corners = []
edge_tiles = []

for tile in tiles:
    # print(tile.id)
    one_count = 0
    for edge in tile.edges:
        # print(edge, a[edge])
        if a[edge] == 1:
            one_count+=1
    if one_count == 2:
        corners.append(tile.id)
    if one_count <=2:
        edge_tiles.append(tile)
print(corners)
z = 1
for corner in corners:
    z *= corner
print(z)

# print(tile_lookup['#.......##'])

# print(edge_tiles)
# 12x12 square has 264 interior sides = 264 edges should have a count of two
matches = []
for et in edge_tiles:
    for et2 in edge_tiles:
        if et == et2:
            pass
        else:
            for edge in et.edges:
                if edge in et2.edges:
                    if et.id < et2.id:
                        matches.append((et.id, et2.id, et.edges.index(edge), et2.edges.index(edge)))
                if edge[::-1] in et2.edges:
                    if et.id < et2.id:
                        matches.append((et.id, et2.id, et.edges.index(edge), et2.edges.index(edge[::-1]), "R"))
print(matches)
print(len(matches))

# (2371, 2593, 0, 0)

print(edge_lookup[2371])
print(edge_lookup[2593])
placed = []

def build(seed):
    placed.append(seed.id)
    currLoc = [0,0]
    for edge in tilemap[seed.id]:
        





build(2833)