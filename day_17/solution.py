import copy
dirs = [(x, y, z, a) for x in range(-1,2) for y in range(-1, 2) for z in range(-1,2) for a in range(-1, 2)]
dirs.remove((0,0,0,0))
rowlen = 24
layer = ["."] * rowlen
supergrid = []
for i in range(rowlen):
    ww = []
    for j in range(rowlen):
        ww.append(".")
    supergrid.append(ww)
# print(supergrid)

old = open("input.txt").read().strip().split("\n")
for i in range(len(old)):
    old[i] = list(old[i])
# print(old)

overall = []

for i in range(13):
    if i == 6:
        # add 3 on each dimension
        # so first it's a 20x6
        # then 6 then first row of old then 6 for 8 rows
        # then a 20x6
        square = []
        for q in range(6):
            ooo = []
            for w in range(rowlen):
                ooo.append(".")
            square.append(ooo)
        for e in range(8):
            ooo = []
            for w in range(6):
                ooo.append(".")
            ooo.extend(old[e])
            for w in range(6):
                ooo.append(".")
            square.append(ooo)
        for q in range(6):
            ooo = []
            for w in range(rowlen):
                ooo.append(".")
            square.append(ooo)
        overall.append(square)
    else:
        p = []
        for j in range(rowlen):
            pp = []
            for u in range(rowlen):
                pp.append(".")
            p.append(pp)
        overall.append(p)

def find_neighbors(arr, z, x, y, a):
    count = 0
    for dz, dx, dy, da in dirs:
        newz = z + dz
        newx = x + dx
        newy = y + dy
        newa = a + da
        # print(newz, newx, newy)
        if 0 <= newy < rowlen and 0 <= newx < rowlen and 0 <= newz < 13:
            if arr[newz][newx][newy] == "#":
                count += 1
    return count

def pretty_print(grid):
    for z in range(13):
        for x in range(rowlen):
            print("".join(grid[z][x]))
        print()


# print(len(overall))





old = overall

# old[10][4][3] = "23423423"



# pretty_print(old)

for i in range(6):
    new_grid = copy.deepcopy(old)
    for z in range(13):
        for x in range(rowlen):
            for y in range(rowlen):
                neighbor_count = find_neighbors(old, z, x, y)
                if old[z][x][y] == "#":
                    print("active", (z,x,y))
                    if 2 <= neighbor_count <= 3:
                        new_grid[z][x][y] = "#"
                    else:
                        new_grid[z][x][y] = "."
                else:
                    if neighbor_count == 3:
                        print("activating", (z,x,y))
                        new_grid[z][x][y] = "#"
                        # print(new_grid[z][x][y], old[z][x][y])
                    else:
                        new_grid[z][x][y] = "."
    # print(i, "\n\n\n\n", new_grid)
    # print(new_grid[7][0][2])
    print("pretty printing new grid")
    pretty_print(new_grid)
    old = new_grid
c = 0
for z in range(13):
    for x in range(rowlen):
        for y in range(rowlen):
            if old[z][x][y] == "#":
                c += 1
print("answer: ", c)

# qwer = [["2", "3"], ["5", "6"]]
# # print("\n".join("".join(qwer)))
# ret = ""
# for row in qwer:
#     ret += "".join(row) + "\n"
# print(ret)

# asdf = ["\n".join("")]