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
    # print(f[current_i])
    save_this = f[current_i]
    # print("current_cup", save_this)
    # print("cups", f)
    next_three = build_next_three(f, current_i)
    # print("pickup", next_three)
    for a in next_three:
        f.remove(a)

    dest_cup = None
    val_to_find = save_this - 1
    while not dest_cup:
        if val_to_find in next_three:
            val_to_find -= 1
        else:
            if val_to_find < smallest:
                val_to_find = biggest
            if val_to_find in f:
                dest_cup = f.index(val_to_find)
                break
    # print("destination:", f[dest_cup])
    add_index = (dest_cup + 1) % 9
    for a in next_three:
        f.insert(add_index, a)
        add_index = (add_index + 1) % 9
    # print("f after: ", f)
    current_i = (f.index(save_this) + 1) % len(f)
# print(f)


def get_answer(f):
    return f[f.index(1) + 1: ] + f[:f.index(1)]


asdfsdaf = get_answer(f)

qq = "".join(str(x) for x in get_answer(f))
print("answer", qq)

# here down was basically copied from reddit holy cow doing it the old way toook forever

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