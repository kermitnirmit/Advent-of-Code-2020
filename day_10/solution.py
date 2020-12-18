import numpy as np
arr = [int(x) for x in open("input.txt").read().rstrip().split("\n")]
arr.append(0)
arr.sort()
arr.append(max(arr) + 3)


def diff_counter(temparr):
    diffs = {1: 0, 2:0, 3:0}
    for i in range(len(temparr) - 1):
        for j in range(1,4):
            if temparr[i] + j in temparr:
                diffs[j] += 1
        # diffs[temparr[i+1] - temparr[i]] += 1
    return diffs

ways_to_finish = {}
def solve(i, temparr):
    if i in ways_to_finish:
        return ways_to_finish[i]
    if i >= len(temparr) - 2:
        ways_to_finish[i] = 1
        return 1
    if i == len(temparr) -3:
        # [x, x+1, x+2] or [x, x+1, x+3] or [x, x+2, x+3]  so you have two ways to get to the end -1
        if temparr[i + 2] - temparr[i] <= 3:
            ways_to_finish[i] = 2
            return 2
        else: # [x + x+3] gives you just one way
            ways_to_finish[i] = 1
            return 1
    num = solve(i + 1, temparr)
    if temparr[i+2] - temparr[i] <= 3:
        num += solve(i+2, temparr)
    if temparr[i+3] - temparr[i] <= 3:
        num += solve(i+3, temparr)
    ways_to_finish[i] = num
    return num

test_arr = arr[:17] + [max(arr[:17]) + 3]


print(solve(0, arr))