import re
import sys

f = open("input.txt").read().strip().split("\n")

# print(f[:2])

# f = ["mask = 000000000000000000000000000000X1001X", "mem[42] = 100", "mask = 00000000000000000000000000000000X0XX","mem[26] = 1"]

mask = f[0].split(" ")[2]


# mem = []
# for w in range(2**36):
#     mem.append(0)

def processval(m, v):
    v = "0" * (36 - len(v)) + v
    ret = []
    for i in range(36):
        if m[i] == "X":
            ret.append(v[i])
        else:
            ret.append(m[i])
    
    return int("".join(ret), 2)


def processaddr(m, a):
    xCount = 0
    indexes = []
    ret = []
    for i in range(36):
        if m[i] == "X":
            ret.append("X")
        elif m[i] == "1":
            ret.append("1")
        else:
            ret.append(a[i])
    for i, x in enumerate(ret):
        if x == "X":
            xCount += 1
            indexes.append(i)
    perms = 2 ** xCount
    raw_addresses = []
    for a in range(perms):
        new_ret = ret.copy()
        binaryRep = str(bin(a))[2:].zfill(xCount)
        for i in range(len(binaryRep)):
            new_ret[indexes[i]] = binaryRep[i]
        raw_addresses.append(new_ret)
    return [int("".join(x), 2) for x in raw_addresses]
    
# print(mask)
# maxM = -1
mem = {}
for i in range(1,len(f)):
    if f[i][:3] == "mem":
        addr, _, val = f[i].split(" ")
        addr = int(addr[4:-1])
        val = int(val)
        strval = str(bin(val))[2:]
        mem[addr] = processval(mask, strval)
    if f[i][:4] == "mask":
        mask = f[i].split(" ")[2]
print("part 1 answer: ", sum(mem.values()))
mem = {}

maxAddr = 0
for i in range(1, len(f)):
    if f[i][:4] == "mask":
        mask = f[i].split(" ")[2]
    if f[i][:3] == "mem":
        addr, _, val = f[i].split(" ")
        addr = int(addr[4:-1])
        val = int(val)

        straddr = str(bin(addr))[2:].zfill(36)
        addrs = processaddr(mask, straddr)
        for q in addrs:
            maxAddr = max(q, maxAddr)
            mem[q] = val
        # print(f"{addr} \t {straddr}")
print("part 2 answer: ", sum(mem.values()))