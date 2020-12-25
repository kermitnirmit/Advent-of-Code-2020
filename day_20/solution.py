from collections import defaultdict
import regex as re
f = open('input.txt').read().strip().split("\n\n")
tiles = {int(p[5:9]): p[11:] for p in open('input.txt').read().strip().split('\n\n')}
flip_tile = lambda p: '\n'.join(l[::-1] for l in p.split('\n'))
rotClockwise = lambda p: '\n'.join(''.join(l[::-1]) for l in zip(*p.split('\n')))
edge = lambda p,i: [p[:10], p[9::11], p[-10:], p[0::11]][i]
def get_all_versions(a):
    b = a
    A = [b]
    for _ in range(3):
        b = rotClockwise(b)
        A.append(b)
    flipped_versions = [flip_tile(q) for q in A]
    A.extend(flipped_versions)
    return A
all_tile_versions = []

for v in tiles.values():
    all_tile_versions.extend(get_all_versions(v))

def match(grid, i):
    versions_of_self = get_all_versions(grid)
    for new_tile in all_tile_versions:
        if new_tile not in versions_of_self:
            if edge(new_tile, (i+ 2 )% 4) == edge(grid, i):
                return new_tile

corners = []
for name, grid in tiles.items():
    c = 0
    for i in range(4):
        if not match(grid, i):
            c += 1
    if c == 2:
        corners.append(name)

q = 1
for a in corners:
    q *= a
print("Part 1: ", q)


corner_tile = next(p for p in get_all_versions(tiles[corners[0]]) if (match(p, 2) and match(p, 3)))

def go_along(grid, i):
    curr = [grid]
    for _ in range(11):
        curr.append(match(curr[-1], i))
    return curr

final_grid = [go_along(w, 3) for w in go_along(corner_tile, 2)]

image = '\n'.join(''.join(a[i:i+8] for a in B[::-1]) for B in final_grid for i in range(12, 99, 11))


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

all_versions_of_image = get_all_versions(image)
gap_to_next_line = '[.#\n]{77}'
look_for = f'#.{gap_to_next_line + "#....#"*3}##{gap_to_next_line}.#{"..#"*5}'
c = 0
for v in all_versions_of_image:
    a = len(re.findall(look_for, v, overlapped=True))
    c+= a
all_hashs = sum(1 for a in image if a == "#")
print("part 2: ", all_hashs - 15 * c)