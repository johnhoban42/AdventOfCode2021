# PART 1
src = open("../inputs/day02.txt").readlines()
src = [s.split(" ") for s in src]
src = [[cmd[0], int(cmd[1])] for cmd in src]
x = 0
y = 0
for dir, n in src:
    if dir == "forward":
        x += n
    elif dir == "up":
        y -= n
    else:  # down
        y += n
ans1 = x * y
print(f"PART 1: {ans1}")

# PART 2
x = 0
y = 0
aim = 0
for dir, n in src:
    if dir == "forward":
        x += n
        y += aim * n
    elif dir == "up":
        aim -= n
    else:  # down
        aim += n
ans2 = x * y
print(f"PART 2: {ans2}")
