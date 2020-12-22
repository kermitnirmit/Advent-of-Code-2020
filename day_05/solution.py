f = open("input.txt").read().rstrip().split("\n")

highest_id = 0
ids = [i for i in range(1024)]
for seat in f:
    l, h = 0, 127
    cl, cr = 0, 7
    for char in seat:
        if char == "F":
            h = (l+h)//2
        if char == "B":
            l = (l + h) // 2 + 1
        if char == "L":
            cr = (cl + cr) // 2
        if char == "R":
            cl = (cl + cr) // 2 + 1
    ids[l * 8 + cl] = "X"
    highest_id = max(l * 8 + cl, highest_id)
print (highest_id)
print([seat for i, seat in enumerate(ids) if 1 <= i <= len(ids) - 2 and seat != "X" and ids[i - 1] == ids[i + 1]][0])
