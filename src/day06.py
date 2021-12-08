from typing import List


# Sim a single lanternfish. Maintain a cache of results, where cache[i] ->
# number of fish produced when a fish reproduces for the first time on day i
def sim_lanternfish(timer: int, days: int, cache: List[int]):
    days -= (timer + 1)
    if days < 0:  # no time to reproduce
        return 1
    elif cache[days] != -1:  # cache hit
        return cache[days]
    fish = 1
    for d in range(days, -1, -7):  # spawn a new lanternfish every 7 days
        fish += sim_lanternfish(8, d, cache)
    cache[days] = fish
    return fish


# Sim a collection of lanternfish using the DP algorithm in sim_lanternfish()
def sim_lanternfish_list(fishes: List[int], days: int):
    fish = 0
    cache = [-1] * days
    for timer in fishes:
        fish += sim_lanternfish(timer, days, cache)
    return fish


# Parse source and sim
src = list(map(int, open("../inputs/day06.txt").read().split(",")))
fish1 = sim_lanternfish_list(src, 80)
fish2 = sim_lanternfish_list(src, 256)

print(f"PART 1: {fish1}")
print(f"PART 2: {fish2}")
