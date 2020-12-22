f = open("input.txt").read().rstrip().split("\n")
act = [int(x) for x in f]
preamble = act[:25]
print(len(preamble))

# for i in range(25, len(act)):
#     num = act[i]
#     found = False
#     for j in preamble:
#         if (act[i] - j) in preamble and (act[i] - j) != j:
#             found = True
#     if found:
#         preamble.pop(0)
#         preamble.append(act[i])
#     else:
#         print(preamble, i)
#         print(act[i])
#         break

target = 41682220

i = 1
curr = act[0]
start = 0
while i <= len(act):
    while curr > target and start < i - 1:
        curr -= act[start]
        start += 1
    if curr == target:
        arr_to_return = act[start: i]
        print(sum(arr_to_return))
        print("answer: ", min(arr_to_return) + max(arr_to_return))
    if i < len(act):
        curr += act[i]
    i += 1
