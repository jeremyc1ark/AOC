import itertools
import math

def make_num_array(string):
    array = list(string)
    return [int(x) for x in array]

data = open('input.txt', 'r').read().strip('\n').split('\n')
data = [make_num_array(x) for x in data]

# Origin is top left corner
# x moves laterally
# y moves vertically
# Duh
x_max = len(data[0]) - 1
x_range = range(x_max)

y_max = len(data) - 1
y_range = range(y_max)


def coord_in_range(x, y):
    return 0 <= x <= x_max and 0 <= y <= y_max

def index(x, y):
    return data[y][x]

def get_adjacent_coords(x, y):
    adjacent_coords = [
        (x+1, y),
        (x, y+1),
        (x-1, y),
        (x, y-1)
    ]
    return list(filter(lambda coord: coord_in_range(*coord), adjacent_coords))

def find_adjacent(x, y):
    adjacent_coords = get_adjacent_coords(x, y)
    return [index(*coord) for coord in adjacent_coords]

def risk_level(x, y):
    point = index(x, y)
    if point < min(find_adjacent(x, y)):
        return point + 1
    return 0

def part_1():
    total_risk = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            total_risk += risk_level(x, y)
    return total_risk

def basin_size(x, y):
    visited_coords = {(x, y)}
    def new_territory(x, y):
        nonlocal visited_coords
        smoke_value = index(x, y)
        adjacent_coords = get_adjacent_coords(x, y)
        adjacent_coords = list(filter(lambda x: x not in visited_coords, adjacent_coords))
        adjacent_pair = [(coord, index(*coord)) for coord in adjacent_coords]
        territory = set()
        for coord, value in adjacent_pair:
            if value == 9:
                continue
            if value > smoke_value:
                territory.add(coord)
        if territory:
            visited_coords = visited_coords.union(territory)
            for coord in territory:
                new_territory(*coord)
    new_territory(x, y)
    return len(visited_coords)

def part_2():
    basin_sizes = list()
    for y in y_range:
        for x in x_range:
            risk = risk_level(x, y)
            if risk:
                size = basin_size(x, y)
                basin_sizes.append(size)
    return math.prod(sorted(basin_sizes, reverse=True)[0:3])

if __name__ == '__main__':
    print(part_1())
    print(part_2())
