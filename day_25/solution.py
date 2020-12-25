f = open('input.txt').read().strip().split("\n")
mod = 20201227


pk1, pk2 = int(f[0]), int(f[1])

def find_loop_size(i, pk):
    ls = 1
    while pow(i, ls, mod) != pk:
        ls += 1
        if ls % 1000000 == 0:
            print("progress", ls)
    return ls

lscard = 13330548 # lscard = find_loop_size(7, pk1)


print(pow(pk2, lscard, mod))