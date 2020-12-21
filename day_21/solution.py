from collections import defaultdict
f = open("input.txt").read().strip().split("\n")

lines = []
for rec in f:
    a,b = rec.split(" (")
    b = b.strip("()").split(", ")
    b[0] = b[0][len("contains") + 1:]
    lines.append((a.split(" "), b))


allergenmap = defaultdict(list)
ingmap = defaultdict(set)

for ing, al in lines:
    for a in al:
        allergenmap[a].append(ing)
        for i in ing:
            ingmap[i].add(a)
    
not_possible = set()
possibles = defaultdict(list)
for ing, al in ingmap.items():
    valid = True
    for a in al:
        if all(ing in anl for anl in allergenmap[a]):
            valid = False
            possibles[ing].append(a)
    if valid:
        not_possible.add(ing)
count = 0
for ing, a in lines:
    for ii in ing:
        if ii in not_possible:
            count += 1
print(count)
while any(len(v) != 1 for v in possibles.values()):
    for ing in possibles:
        if len(possibles[ing]) == 1:
            first = next(iter(possibles[ing]))
            for k, v in possibles.items():
                if k == ing:
                    pass
                else:
                    if first in v: v.remove(first)

print((",".join([x[0] for x in sorted(list(possibles.items()), key = lambda x : x[1])])))