f = open('input.txt').read().strip().split("\n\n")


origp1 = [int(x) for x in f[0].split("\n")[1:]]
origp2 = [int(x) for x in f[1].split("\n")[1:]]
p1 = origp1.copy()
p2 = origp2.copy()
while (len(p1) > 0 and len(p2) > 0):
    a = p1.pop(0)
    b = p2.pop(0)
    if a > b:
        p1.extend([a, b])
    else:
        p2.extend([b, a])
if len(p1) == 0:
    q = 0
    for i, x in enumerate(p2[::-1]):
        q += (i + 1) * x
    print(q)
    # print sum([(i + 1) * x for i, x in enumerate(p2[::-1])])
if len(p2) == 0:
    # print sum([(i + 1) * x for i, x in enumerate(p1[::-1])])
    q = 0
    for i, x in enumerate(p1[::-1]):
        q += (i + 1) * x
    print(q)


def subgame(p1cards, p2cards):
    while(len(p1cards) > 0 and len(p2cards) > 0):
        print("subgame", p1cards)
        print("subgame", p2cards)
        input("enter to continue")
        a, b = p1cards.pop(0), p2cards.pop()
        if len(p1cards) >= a and len(p2cards) >= b:
            winner = subgame(p1cards[:1+a], p2cards[:1+b])
        else:
            winner = 1 if a > b else 0
        if winner == 1:
            p1cards.extend([a, b])
        else:
            p2cards.extend([b, a])
# visited = set()
def war(p1cards, p2cards, visited):
    while(len(p1cards) > 0 and len(p2cards) > 0):
        if (tuple(p1cards), tuple(p2cards)) in visited:
            return 1, p1cards
        visited.add((tuple(p1cards), tuple(p2cards)))
        a, b = p1cards.pop(0), p2cards.pop(0)
        if len(p1cards) >= a and len(p2cards) >= b:
            winner, _ = war(p1cards[:a], p2cards[:b], set())
        else:
            winner = 1 if a > b else 0
        if winner == 1:
            p1cards.extend([a, b])
        else:
            p2cards.extend([b, a])
    if len(p1cards) > 0:
        return 1, p1cards
    else:
        return 0, p2cards
_, winningCards = war(origp1, origp2, set())

q = 0
for i, x in enumerate(winningCards[::-1]):
    q += (i + 1) * x
print(q)
