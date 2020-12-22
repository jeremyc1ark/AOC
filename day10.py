from functools import lru_cache
from time import time

data = open('input.txt', 'r').read().strip().split('\n')
data = set(map(int, data))
data.add(max(data) + 3)

def part_1(input_data, current_jolt=0, jolt_diffs={1:0,1:0,3:0}):
    options = set(map(lambda x: current_jolt + x, range(1,4))).intersection(input_data)
    if not options:
        return jolt_diffs[1] * jolt_diffs[3]
    next_jolt = min(options)
    jolt_diffs[next_jolt-current_jolt] += 1
    return part_1(input_data, next_jolt, jolt_diffs)

def part_2(input_data):
    @lru_cache
    def helper(current):
        options = set(map(lambda x: current + x, range(1,4))).intersection(input_data)
        if not options:
            return 1
        return sum(map(lambda x: helper(x), options))
    return helper(0)
