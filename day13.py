from sympy.ntheory.modular import crt
import re
from copy import copy

data = open('input.txt', 'r').read().strip().split('\n')
data[0] = int(data[0])
data[1] = list(map(
    lambda y: int(y) if bool(re.match(r'\d+', y)) else y,
    re.findall(r'\d+|x', data[1])))

def part_1(input_data):
    local_data = list(filter(lambda y: isinstance(y, int), input_data))
    original_timestamp, bus_ids = local_data
    can_catch = lambda bus_id, timestamp: timestamp % bus_id == 0
    current_timestamp = copy(original_timestamp)
    arrivals = list()

    while not arrivals:
        current_timestamp += 1
        arrivals = list(filter(lambda x: can_catch(x, current_timestamp), bus_ids))

    return arrivals[0] * (current_timestamp - original_timestamp)

def part_2(input_data):
    remainders = list()
    mods = list()

    for i, elem in enumerate(input_data[1]):
        if isinstance(elem, int):
            mods.append(elem)
            remainders.append(-i % elem)

    return crt(mods, remainders)[0]
