import re


# Parse source
src = open("../inputs/day05.txt").readlines()
n = 1000  # seafloor dimensions
floor1 = [0] * (n*n)  # flat representation of an n x n grid, (x, y) -> x + n*y
floor2 = [0] * (n*n)

# PART 1: Record horizontal and vertical vents
# PART 2: Record horizontal, vertical, and diagonal vents
for vent in src:
    v = re.split(",| -> ", vent.strip())
    x1, y1, x2, y2 = map(int, v)
    if x1 != x2 and y1 != y2:  # iterate diagonally
        while True:
            floor2[x1 + n*y1] += 1
            if x1 == x2:  # reached end of vent, stop
                break
            x1 = x1 + 1 if x1 < x2 else x1 - 1
            y1 = y1 + 1 if y1 < y2 else y1 - 1
    elif x1 != x2:  # iterate through x
        while True:
            floor1[x1 + n*y1] += 1
            floor2[x1 + n*y1] += 1
            if x1 == x2:  # reached end of vent, stop
                break
            x1 = x1 + 1 if x1 < x2 else x1 - 1
    else:  # iterate through y
        while True:
            floor1[x1 + n*y1] += 1
            floor2[x1 + n*y1] += 1
            if y1 == y2:  # reached end of vent, stop
                break
            y1 = y1 + 1 if y1 < y2 else y1 - 1

danger1 = list(filter(lambda x: x >= 2, floor1))
danger2 = list(filter(lambda x: x >= 2, floor2))
print(f"PART 1: {len(danger1)}")
print(f"PART 2: {len(danger2)}")
