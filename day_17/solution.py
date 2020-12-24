from tqdm import trange
from collections import defaultdict
dirs = [(x, y, z, a) for x in range(-1,2) for y in range(-1, 2) for z in range(-1,2) for a in range(-1, 2)]
dirs.remove((0,0,0,0))

original = [list(x) for x in open("input.txt").read().strip().split("\n")]
# for i in range(len(original)):
#     original[i] = list(original[i])


old = defaultdict(lambda x : False)

for i in range(len(original)):
    for j in range(len(original[i])):
        if original[i][j] == "#":
            old[(i, j, 0, 0)] = True
        else:
            old[(i,j,0,0)] = False
neighbors_to_add = set((x + dx, y + dy, z + dz, a + da) for dx, dy, dz, da in dirs for x,y,z,a in list(old.keys()) if old[x,y,z,a])
for q in neighbors_to_add:
    if q not in old:
        old[q] = False

def find_neighbors(locs, loc):
    x,y,z,a = loc
    c = 0
    for dx, dy, dz, da in dirs:
        new_pos = (x + dx, y + dy, z + dz, a + da)
        if new_pos in locs:
            if locs[new_pos]:
                c += 1
    return c
for _ in trange(6):
    new_one = {}
    for loc, v in old.items():
        n = find_neighbors(old, loc)
        if v:
            if n == 2 or n == 3:
                new_one[loc] = v
            else:
                new_one[loc] = False
        else:
            if n == 3:
                new_one[loc] = True
            else:
                new_one[loc] = v
    neighbors_to_add = set((x + dx, y + dy, z + dz, a + da) for dx, dy, dz, da in dirs for x,y,z,a in list(new_one.keys()) if new_one[x,y,z,a])
    for q in neighbors_to_add:
        if q not in new_one:
            new_one[q] = False
    old = new_one

print(sum(old.values()))