# N, E, S, W, NE, NW, SE, NW
dirs = [(0,1), (1,0), (0, -1), (-1, 0)]

mapping = {"N": 0, "E": 1, "S": 2, "W": 3}


f = [(x[0], int(x[1:])) for x in open("input.txt").read().rstrip().split("\n")]

# # f = [("F", 10), ("N", 10), ("E", 15), ("F", 10)]
# f = [("F", 1), ("L", 90)]

original_pos = [0, 0]
current_pos = [0,0]
current_dir = dirs[1]
waypoint = [10,1]
for direction, dist in f:
    # if direction == "F":
    #     current_pos[0] += dist * current_dir[0]
    #     current_pos[1] += dist * current_dir[1]
    
    # if direction in "LR":
    #     if direction == "L":
    #         new_index = (dirs.index(current_dir) - dist // 90) % 4
    #         current_dir = dirs[new_index]
    #     if direction == "R":
    #         new_index = (dirs.index(current_dir) + dist // 90) % 4
    #         current_dir = dirs[new_index]
    # if direction in "NSEW":
    #     dirtomove = dirs[mapping[direction]]
    #     current_pos[0] += dirtomove[0] * dist
    #     current_pos[1] += dirtomove[1] * dist
    # print(direction, dist, current_dir, current_pos)

    # part 2:
    if direction == "F":
        current_pos[0] += dist * waypoint[0]
        current_pos[1] += dist * waypoint[1]
    if direction in "NSEW":
        dirtomove = dirs[mapping[direction]]
        waypoint[0] += dist * dirtomove[0]
        waypoint[1] += dist * dirtomove[1]
    if direction in "LR":
        if (direction == "L" and dist == 90) or (direction == "R" and dist == 270):
            waypoint = [-1 * waypoint[1], waypoint[0]] 
        elif dist == 180:
            waypoint = [-1* waypoint[0], -1 * waypoint[1]]
        else:
            waypoint = [waypoint[1], -1 * waypoint[0]]

print(waypoint)

print(abs(current_pos[0]) + abs(current_pos[1]))