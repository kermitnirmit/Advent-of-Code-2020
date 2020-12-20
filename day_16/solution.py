import numpy
f = open("input.txt").read().strip().split("\n")

overallRanges = numpy.zeros(1000, numpy.int8)

ranges = {}

for a in f[:20]:
    asdf = a.split(" ")
    s = asdf[-3:]
    indRange = numpy.zeros(1000, numpy.int8)
    leftRangeMin, leftRangeMax = int(s[0].split("-")[0]), int(s[0].split("-")[1])
    rightRangeMin,rightRangeMax = int(s[2].split("-")[0]), int(s[2].split("-")[1])
    indRange[leftRangeMin:leftRangeMax + 1] = 1
    overallRanges[leftRangeMin:leftRangeMax + 1] = 1
    indRange[rightRangeMin:rightRangeMax + 1] = 1
    overallRanges[rightRangeMin:rightRangeMax + 1] = 1
    ranges[" ".join(asdf[:-3])] = indRange
# print(ranges.items())
failed = 0
validTix = []
for line in f[25:]:
    failure = False
    for number in line.split(","):
        if overallRanges[int(number)] == 0:
            # failed
            failure = True
            break
    if not failure:
        validTix.append([int(x) for x in line.split(",")])

# print(len(f[25:]) - len(validTix))
validFields = list(ranges.keys())

# while len(validFields) > 0:
#     for ticket in validTix:
#         for field in validFields:
#             if ranges[field][ticket[12]] == 0:
#                 validFields.remove(field)
#                 break
#         print(validFields)

order = []
for i in range(20):
    vf = validFields.copy()
    for ticket in validTix:
        for field in vf:
            if ranges[field][ticket[i]] == 0:
                vf.remove(field)
                break
    order.append((i, vf, len(vf)))
    # print(i, vf, len(vf))

# print(order)
order.sort(key = lambda x: x[2])

# use process of elimination for this :D
for q in order:
    print(q)
# index 11 is class
# index 19 is route
# index 15 is price
# index 12 is arrival location
# index 13 is duration
# index 8 is dep platform ***
# index 7 is dep track ***
# index 0 is dep time ***
# index 3 is dep station ***
# index 1 is dep locaiton ***
# index 14 is dep date ***

my_ticket = [int(x) for x in f[22].split(",")]
print(my_ticket[8] * my_ticket[7] * my_ticket[0] * my_ticket[3] * my_ticket[1] * my_ticket[14])
