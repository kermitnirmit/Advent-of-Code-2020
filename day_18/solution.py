f = open("input.txt").read().strip().split("\n")


class N1:
    def __init__(self, v):
        self.v = v

    def __add__(self, num):
        return N1(self.v + num.v)

    def __sub__(self, num):
        return N1(self.v * num.v)
rsum = 0
for l in f:
    out = "".join("N1("+x+")" if x.isdigit() else x for x in l)
    out = out.replace("*", "-")
    rsum += eval(out).v
print(rsum)


class N2:
    def __init__(self, v):
        self.v = v
    def __add__(self, num):
        return N2(self.v * num.v)
    def __mul__(self, num):
        return N2(self.v + num.v)

rsum2 = 0
for l in f:
    out = "".join("N2("+x+")" if x.isdigit() else x for x in l)
    out = out.replace("+", "?").replace("*", "+").replace("?", "*")
    rsum2 += eval(out).v
print(rsum2)