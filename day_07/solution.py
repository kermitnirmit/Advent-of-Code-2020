from collections import defaultdict
f = open("input.txt").read().rstrip().split("\n")

bags_dict = {}

bag_creators = defaultdict(set)

for rule in f:
    bags, contains = rule[:-1].split("contain")
    within = contains.lstrip().split(", ")
    color = bags[:-5]
    color = color.strip()
    children = []
    for b in within:
        temp = b.split(" ")
        if len(temp) == 3:
            continue
        mult = temp[0]
        cc = " ".join(temp[1:3])
        children.append(cc)
        if color in bags_dict:
            bags_dict[color].append((int(mult), cc))
        else:
            bags_dict[color] = [(int(mult), cc)]
    for c in children:
        bag_creators[c].add(color)

def part_1(visited, creators, node):
    num_to_send_up = 1
    if node in visited:
        return 0
    else:
        visited.add(node)
        for creator in creators[node]:
            num_to_send_up += part_1(visited, creators, creator)
    return num_to_send_up

visited = set()
def dfs(bags_dict, node):
    num_to_send_up = 0
    if node not in bags_dict:
        return 0
    for factor, neighbor in bags_dict[node]:
        # print(factor, neighbor, num_to_send_up)
        num_to_send_up += factor * (1+ dfs(bags_dict, neighbor))
    return num_to_send_up


print(part_1(visited, bag_creators, "shiny gold") - 1)
visited = set()
print(dfs(bags_dict, "shiny gold"))