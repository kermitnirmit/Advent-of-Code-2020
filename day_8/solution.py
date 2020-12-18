f = open("input.txt").read().rstrip().split("\n")
instructions = []
for line in f:
    inst, num = line.split(" ")
    instructions.append((inst, int(num)))
i = 0
indexes = []
for index, asdf in enumerate(instructions):
    inst, num = asdf

    if inst != "acc":
        indexes.append(index)
# print(indexes)
# visited = set()
# acc_val = 0

# def get_answer():
#     visited = set()
#     acc_val = 0
#     i = 0
#     while i > -1:
#         if i in visited:
#             return acc_val
#         else:
#             visited.add(i)
#             inst, num = instructions[i]
#             if inst == "acc":
#                 acc_val += num
#                 i += 1
#             elif inst == "jmp":
#                 i += num
#             else:
#                 i += 1

# print(get_answer())
answers = []
print(instructions)
last_index = len(instructions)
def modified_answer(index):
    visited = set()
    acc_val = 0
    i = 0
    while i > -1:
        if i in visited:
            return [acc_val]
        if i == last_index:
            return "completed", acc_val
        if i == index:
            visited.add(i)
            inst, num = instructions[i]
            if inst == "acc":
                acc_val += num
                i += 1
            elif inst == "jmp":
                i += 1
            else:
                i += num
        else:
            visited.add(i)
            inst, num = instructions[i]
            if inst == "acc":
                acc_val += num
                i += 1
            elif inst == "jmp":
                i += num
            else:
                i += 1

for index in indexes:
    a = modified_answer(index)
    if len(a) == 2:
        print(a)


