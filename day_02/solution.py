f = open("input.txt").read().strip().split("\n")

p1count = p2count = 0
for line in f:
    l, text = line.split(":")
    text = text.strip()
    rang, letter = l.split()
    low, high = rang.split("-")
    low, high = int(low), int(high)
    if low <= text.count(letter) <= high:
        p1count+= 1
    if (text[low - 1] == letter) != (text[high - 1] == letter):
        p2count+= 1
print(p1count)
print(p2count)