# PART 1
src = list(map(int, open("../inputs/day01.txt").readlines()))
ans1 = 0
for i in range(len(src) - 1):
    if src[i] < src[i+1]:
        ans1 += 1
print(f"PART 1: {ans1}")

# PART 2
window = sum(src[0:3])
ans2 = 0
for i in range(3, len(src)):
    new_window = window - src[i-3] + src[i]
    if window < new_window:
        ans2 += 1
    window = new_window
print(f"PART 2: {ans2}")
