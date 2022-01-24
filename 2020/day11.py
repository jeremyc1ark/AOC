from itertools import product
from copy import copy
data = open('input.txt', 'r').read().strip().split('\n')

def in_range(x, y, horz, vert):
    return 0 <= x <= horz and 0 <= y <= vert

def access(chart, x, y):
    return chart[y][x]

def replacement(x, y, leaving_func, occupy_func, chart):
    char = access(chart, x, y)
    if char == '.':
        return '.'
    if char == '#':
        return leaving_func(x, y, chart)
    if char == 'L':
        return occupy_func(x, y, chart)

def one_cycle(chart, leaving_func, occupy_func):
    new_chart = list()
    for i, elem in enumerate(chart):
        row = str()
        for j in range(0, len(elem)):
            row += replacement(j, i, leaving_func, occupy_func, chart)
        new_chart.append(row)
    return new_chart

def is_status(x, y, chart, status):
    vert = len(chart) - 1
    horz = len(chart[0]) - 1
    return in_range(x, y, horz, vert) and access(chart, x, y) == status


def part_1(input_data, prev_data=None):
    def get_coord_list(x, y):
        x_options = (x-1, x, x+1)
        y_options = (y-1, y, y+1)
        coord_list = [(a, b) for a in x_options for b in y_options]
        coord_list.remove((x, y))
        return coord_list

    def should_occupy(x, y, chart):
        for coord in get_coord_list(x, y):
            if not is_status(*coord, chart, '#'):
                continue
            return 'L'
        return '#'

    def should_leave(x, y, chart):
        seats = 0
        for coord in get_coord_list(x, y):
            if is_status(*coord, chart, '#'):
                seats += 1

        if seats >= 4 and is_status(x, y, chart, '#'):
            return 'L'
        return '#'


    if prev_data == input_data:
            return sum(map(lambda x: x.count('#'), input_data))
    return part_1(one_cycle(input_data, should_leave, should_occupy), input_data)

def part_2(input_data, prev_data=None):
    def num_seen_seats(x, y, chart):
        horz = len(chart[0]) - 1
        vert = len(chart) - 1
        num_seats = 0

        def take_step(coord_dict):
            for key in coord_dict.keys():
                x, y = key
                i, j = coord_dict[key]
                coord_dict[key] = (x+i, y+j)

        adders = list(product([-1, 1, 0], repeat=2))
        adders.remove((0, 0))
        coords = dict(zip(adders, [(x, y)] * 8))
        take_step(coords)

        while coords:
            for adder, coord in copy(coords).items():
                if not in_range(*coord, horz, vert):
                    del coords[adder]
                    continue
                current_spot = access(chart, *coord)
                if current_spot == '#':
                    num_seats += 1
                    del coords[adder]
                elif current_spot == 'L':
                    del coords[adder]
            take_step(coords)
        return num_seats

    def should_leave(x, y, chart):
        if num_seen_seats(x, y, chart) > 4 and is_status(x, y, chart, '#'):
            return 'L'
        return '#'

    def should_occupy(x, y, chart):
        if num_seen_seats(x, y, chart) == 0 and is_status(x, y, chart, 'L'):
            return '#'
        return 'L'

    # return one_cycle(input_data, should_leave, should_occupy)
    if prev_data == input_data:
        return sum(map(lambda x: x.count('#'), input_data))
    return part_2(one_cycle(input_data, should_leave, should_occupy), input_data)

