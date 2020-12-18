f = open("input.txt").read().rstrip().split("\n")

class Bag:
    can_be_created_by = []
    color = ""
    def __init__(self, color, can_be_created_by):
        self.can_be_created_by = can_be_created_by
        self.color = color
    def add_creator(self, bag):
        self.can_be_created_by.append(bag)

bags_dict = {}
# for rule in f:
#     bags, contains = rule[:-1].split("contain")
#     within = contains.lstrip().split(",")
#     color = bags[:-5]
#     color = color.strip()
#     # print(color, within)
#     for b in within:
#         # no other bags
#         if len(b.strip().split(" ")) == 3:
#             break
#         qwe = b.strip().split(" ")
#         # print(qwe)
#         ww = " ".join(qwe[1:3])
#         ww = ww.strip()
#         # print(color, ww)
#         if ww in bags_dict:
#             bags_dict[ww].append(color.strip())
#         else:
#             bags_dict[ww] = [color.strip()]
# # print(bags_dict)
# count = 0
# visited = set()
# bfs_queue = []

# visited.add("shiny gold")
# bfs_queue.append("shiny gold")

# while bfs_queue:
#     s = bfs_queue.pop(0)
#     if s not in bags_dict:
#         continue
#     for creator in bags_dict[s]:
#         if creator not in visited:
#             visited.add(creator)
#             bfs_queue.append(creator)
#             count += 1
# print(count)

for rule in f:
    bags, contains = rule[:-1].split("contain")
    within = contains.lstrip().split(", ")
    color = bags[:-5]
    color = color.strip()
    # print(color, within)
    for b in within:
        temp = b.split(" ")
        if len(temp) == 3:
            continue
        mult = temp[0]
        cc = " ".join(temp[1:3])
        # print(mult, cc)
        if color in bags_dict:
            bags_dict[color].append((int(mult), cc))
        else:
            bags_dict[color] = [(int(mult), cc)]

# print(bags_dict)

visited = set()
def dfs(visited, bags_dict, node):
    num_to_send_up = 0
    if node not in bags_dict:
        return 0
    for factor, neighbor in bags_dict[node]:
        print(factor, neighbor, num_to_send_up)
        num_to_send_up += factor * (1+ dfs(visited, bags_dict, neighbor))
    return num_to_send_up

print(dfs(visited, bags_dict, "shiny gold"))