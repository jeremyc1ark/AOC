import itertools

data = open('input.txt', 'r').read().split('\n')
data = list(filter(lambda x: bool(x), data))
data = list(map(int, data))


def part_1(lat):
    def sum_to_2020(a, b):
        return a + b == 2020

    for i, j in itertools.product(lat, lat):
        if sum_to_2020(i, j):
            return i * j
    return False

def part_2(lat):
    def sum_to_2020(a, b, c):
        return a + b + c == 2020

    for i, j, k in itertools.product(lat, lat, lat):
        if sum_to_2020(i, j, k):
            return i * j * k
    return False
