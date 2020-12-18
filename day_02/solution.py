import re
f = open("input.txt", "r")

asd = [x for x in f]

rcount = 0
for line in asd:
    l, text = re.split(r":", line)
    text = text.strip()
    rang, letter = re.split(r" ", l)
    low, high = re.split(r"-", rang)
    low = int(low)
    high = int(high)
    # print (low, high, letter, text.strip())
    # Puzzle 1
    # if low <= text.count(letter) <= high:
    #     rcount+= 1
    if (text[low - 1] == letter) != (text[high - 1] == letter):
        rcount+= 1
print(rcount)