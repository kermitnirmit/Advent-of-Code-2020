
dirs = [(0,1), (1,0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

f = open("input.txt").read().rstrip().split("\n")

old = f
new = [[]]

def count_adjacent(arr, i, j):
    # occupied is #
    occupied = 0
    for x, y in dirs:
        newx, newy = i + x, j + y
        if 0 <= newx < len(arr) and 0 <= newy < len(arr[0]) and arr[newx][newy] == "#":
            occupied += 1
    return occupied

def count_visible(arr, i, j):
    occupied = 0
    for x,y in dirs:
        newx, newy = i + x, j + y
        found = False
        while 0 <= newx < len(arr) and 0 <= newy < len(arr[0]) and not found:
            if arr[newx][newy] == "#":
                occupied += 1
                found = True
            elif arr[newx][newy] == "L":
                found = True
            else:
                newx, newy = newx + x, newy + y
    return occupied
while 1:
    new = []
    for i in range(len(f)):
        templine = []
        for j in range(len(f[i])):

            # part 1
            # ad = count_adjacent(old, i, j)

            # part 2
            ad = count_visible(old, i, j)
            if old[i][j] == "L" and ad == 0:
                templine.append("#")
            elif old[i][j] == "#" and ad >= 5:
                templine.append("L")
            else:
                templine.append(old[i][j])
        new.append(templine)
    if old == new:
        count = 0
        for i in new:
            for j in i:
                if j == "#":
                    count += 1
        print(count)
        break
    old = new


