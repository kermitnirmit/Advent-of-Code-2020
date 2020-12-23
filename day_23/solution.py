from tqdm import tqdm
f = [int(x) for x in str(247819356)]
origf = f.copy()
# 

# mine 247819356 
# print(f)

def build_next_three(qwer, index):
    ret =[]
    i = (index + 1) % len(qwer)
    while(len(ret) != 3):
        ret.append(qwer[i])
        i  = (i + 1) % len(qwer)
    return ret

smallest, biggest = min(f), max(f)
current_i = 0
for move in range(100):
    save_this, next_three = f[current_i], build_next_three(f, current_i)
    
    for a in next_three:
        f.remove(a)
    
    dest_cup, val_to_find = None, save_this - 1
    seen = set(next_three)
    seen.add(save_this)
    while val_to_find in next_three:
        val_to_find -= 1
    if val_to_find == 0:
        val_to_find = max(f)
    dest_cup = f.index(val_to_find)

    add_index = (dest_cup + 1) % 9
    for a in next_three:
        f.insert(add_index, a)
        add_index = (add_index + 1) % 9
    current_i = (f.index(save_this) + 1) % len(f)

print("answer", "".join(str(x) for x in f[f.index(1) + 1: ] + f[:f.index(1)]))

# credit @nthistle for helping me unfuck my errors in this

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"({self.val})"

revLookup = {}

node_list = [Node(v) for v in origf]


cur = len(origf) + 1

while len(node_list) < 1000000:
    node_list.append(Node(cur))
    cur += 1

for a,b in zip(node_list, node_list[1:]):
    a.next = b

node_list[-1].next = node_list[0]

for node in node_list:
    revLookup[node.val] = node
start = node_list[0]
for move in tqdm(range(10000000)):
    first = start.next
    second = first.next
    third = second.next
    start.next = third.next
    val_to_find = start.val
    while val_to_find in {first.val, second.val, third.val, start.val}:
        val_to_find -= 1
        if val_to_find < 1:
            val_to_find = 1000000
    dest = revLookup[val_to_find]
    after = dest.next
    dest.next = first
    third.next = after
    start = start.next

# find 1
one = revLookup[1]
a = one.next
b = a.next

print("answer:", a.val * b.val)