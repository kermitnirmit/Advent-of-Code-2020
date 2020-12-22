groups = open("input.txt").read().rstrip().split("\n\n")

# q1
print(sum(len(set(i.replace("\n", ""))) for i in groups))

# q2
# print(groups)
qwer = []
for group in groups:
    e = group.split("\n")
    q = [set(q) for q in e]
    qwer.append((len(q[0].intersection(*q))))
print(sum(qwer))
