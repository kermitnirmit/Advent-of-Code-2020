f = [12,1,16,3,11,0]

def rindex(li, val):
    return len(li) - li[::-1].index(val) - 1

last_indexes = {}
for index , val in enumerate(f[:-1]):
    last_indexes[val] = index


for i in range(len(f) - 1, 30000000 - 1):
    if f[-1] not in last_indexes:
        last_indexes[f[-1]] = i
        f.append(0)
    else:
        last_time = last_indexes[f[-1]]
        last_indexes[f[-1]] = i
        f.append(i - last_time)
print(f[-1])