f = open("input.txt", "r")

entries = sorted([int(x) for x in f])


# # Problem 1
# for entry in all_entries:
#     if 2020 - entry in all_entries:
#         print( entry * (2020 - entry))
#         break
count = len(entries)

for i in range(count- 2):
    l, r = i + 1, count - 1
    while l < r:
        if entries[i] + entries[l] + entries[r] == 2020:
            print(entries[i] * entries[l] * entries[r])
            break
        elif  entries[i] + entries[l] + entries[r] > 2020:
            r-=1
        else:
            l += 1
print("none found")


# print(len(all_entries))