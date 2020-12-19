from math import gcd
f = open("input.txt").read().strip().split("\n")

est = int(f[0])
buses = []

for i, x in enumerate(f[1].split(",")):
    if x.isdigit():
        buses.append((i, int(x)))
print(buses)

def compute_lcm(x, y):
    return x * y // gcd(x,y)


lcm = buses[0][1]
for _, i in buses[1:]:
    lcm = lcm * i // gcd(lcm, i)


smallLCM = buses[0][1]
index = 1

i = buses[0][1]

while i < lcm:
    offset, busID = buses[index]
    if (i + offset) % busID == 0:
        print("match found: ", i)
        index += 1
        if index >= len(buses):
            print("answer: ", i)
        smallLCM = compute_lcm(smallLCM, busID)
    i += smallLCM
