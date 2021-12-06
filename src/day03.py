# PART 1
src = open("../inputs/day03.txt").read().split("\n")
n = len(src)  # lines
k = len(src[0])  # bits per line
gamma = 0
epsilon = 0
for i in range(k):
    gamma <<= 1
    epsilon <<= 1
    if sum(int(x[i]) for x in src) > n / 2:
        gamma += 1
    else:
        epsilon += 1
print(f"PART 1: {gamma * epsilon}")

# PART 2
o2list = src.copy()
i = 0
while i < k and len(o2list) > 1:
    bit = '1' if sum(int(x[i]) for x in o2list) >= len(o2list) / 2 else '0'
    o2list = list(filter(lambda x: x[i] == bit, o2list))
    i += 1
co2list = src.copy()
i = 0
while i < k and len(co2list) > 1:
    bit = '0' if sum(int(x[i]) for x in co2list) >= len(co2list) / 2 else '1'
    co2list = list(filter(lambda x: x[i] == bit, co2list))
    i += 1
print(f"PART 2: {int(o2list[0], 2) * int(co2list[0], 2)}")
