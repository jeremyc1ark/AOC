import numpy as np
from scipy.ndimage import generic_filter

# Solution inspired by @r0f1
# https://github.com/r0f1/adventofcode2020/blob/master/day17/main.py

with open('input.txt') as lines:
    data = [list(x.strip()) for x in lines]
    data = (np.array(data) == '#').astype(np.uint8)

def increase_dims(plane, dims):
    space = plane
    for _ in range(dims-2):
        space = np.reshape(space, (1,) + space.shape)
    return space

def next_state(community):
    community_sum = np.sum(community)
    if community[len(community) // 2]:
        return int(community_sum in (3, 4))
    return int(community_sum == 4)

def pad_space(space, padding_amount):
    return np.pad(space, padding_amount)

def make_kernel(dims):
    return np.ones((((3,) * dims)), dtype=np.uint8)

def one_cycle(space, kernel):
    return generic_filter(space, next_state, footprint=kernel, mode='constant', cval=0)

def conway_cubes(plane, dims, repetitions):
    space = pad_space(increase_dims(plane, dims), 10)
    kernel = make_kernel(dims)
    for _ in range(repetitions):
        space = one_cycle(space, kernel)
    return np.sum(space)

part_1 = conway_cubes(data, 3, 6)
part_2 = conway_cubes(data, 4, 6)
