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
# for every ingredient and allergen list (each line)
for ing, al in lines:
    # for every allergen, add the list of possible ingredients it could be
    for a in al:
        allergenmap[a].append(ing)
        # for every ingredient, add the allergens in that line
        for i in ing:
            ingmap[i].add(a)
    
not_possible = set()
possibles = defaultdict(list)
# for each ingredient and the possible allergens
for ing, al in ingmap.items():
    valid = True
    # loop over all of the possible allergens that the ingredient could be
    for a in al:
        # if this ingredient is in each ingredient list that corresponds to this allergen, it's a possible allergen
        if all(ing in anl for anl in allergenmap[a]):
            valid = False
            # add that possible allergen to what ing could be
            possibles[ing].append(a)
    # if not, it can not be an allergen
    if valid:
        not_possible.add(ing)
# simple count of ingredients that are in the not possible
count = 0
for ing, a in lines:
    for ii in ing:
        if ii in not_possible:
            count += 1
print(count)

# remove the ones that are already defined from ones that arent.
while any(len(v) != 1 for v in possibles.values()):
    for ing in possibles:
        if len(possibles[ing]) == 1:
            first = next(iter(possibles[ing]))
            for k, v in possibles.items():
                if k == ing:
                    pass
                else:
                    if first in v: v.remove(first)
# print properly
print(",".join(x[0] for x in sorted(list(possibles.items()), key = lambda x : x[1])))