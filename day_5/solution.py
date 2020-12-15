f = open("input.txt").read().rstrip().split("\n")

highest_id = 0
ids = [i for i in range(1024)]
test = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
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
# print(seat, l, h, cl , cr)
print(ids)
print (highest_id)
