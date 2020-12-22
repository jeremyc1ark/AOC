from functools import reduce
from operator import mul

def circular_index(arr, index):
    return arr[index % len(arr)]

def is_tree(lat_index, lat):
    return circular_index(lat, lat_index) == '#'

def any_slope(x_step, y_step, input_data):
    def helper(x, y, acc):
        if y + y_step > len(input_data) - 1:
            return acc
        return helper(x + x_step, y + y_step, is_tree(x, input_data[y]) + acc)
    return helper(x_step, y_step, 0)

def part_1(input_data):
    return any_slope(3, 1, input_data)

def part_2(input_data, step_pairs):
    """'step_pairs' example:
    [(4, 1), (5, 9), (1, 3)]
    First element of each tuple represents 'x_step'
    Second elemnt of each tuple represents 'y_step'
    """

    return reduce(mul,
                  map(lambda x: any_slope(*x, input_data),
                      step_pairs))

if __name__ == '__main__':
    data = open('input.txt', 'r').read().split('\n')
    data = data[:-1]

    given_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(f"Answer for Part 1: {part_1(data)}")
    print(f"Answer for Part 2: {part_2(data, given_slopes)}")

