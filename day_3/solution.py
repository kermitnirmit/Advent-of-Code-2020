f = open("input.txt", "r")

field = [x.rstrip() for x in f]
treeCount = 0
posh, posx = 0, 0

def try_with_slope(right, down):
    treeCount = 0
    posh, posx = 0, 0
    while posh < len(field):
        if field[posh][posx] == "#":
            # print(posh, posx, "#")
            treeCount += 1
        posh += down
        posx = (posx + right) % len(field[0])

    return treeCount

if __name__ =="__main__":
    a = try_with_slope(1,1)
    b = try_with_slope(3,1)
    c = try_with_slope(5,1)
    d = try_with_slope(7,1)
    e = try_with_slope(1,2)
    print(a,b,c,d,e)
    print (a*b*c*d*e)
