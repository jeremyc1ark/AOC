import re
import collections

data = open('input.txt', 'r').read().strip('\n').split('\n')
data_parser_regex = re.compile('^(\d+),(\d+)\s->\s(\d+),(\d+)$')

def line_to_list(line):
    l = [int(x) for x in data_parser_regex.match(line).groups()]
    return [l[0], l[1], l[2], l[3]]

data = [line_to_list(x) for x in data]

def is_vert_or_horz(v):
    return v[0] == v[2] or v[1] == v[3]

only_vert_and_horz = list(filter(is_vert_or_horz, data))

def get_points_narrow(equality_axis, equality, diff1, diff2):
    point_list = list()
    lo = min((diff1, diff2))
    hi = max((diff1, diff2))
    while lo <= hi:
        if equality_axis == 'x':
            point = (equality, lo)
        else:
            point = (lo, equality)
        point_list.append(point)
        lo += 1
    return point_list

def get_axis(vent):
    x1, y1, x2, y2 = vent
    if x1 == x2:
        return 'x'
    elif y1 == y2:
        return 'y'
    else:
        return 'xy'

def get_points_diag(vent):
    point_list = list()
    x1, y1, x2, y2 = vent
    xmin, xmax, ymin, ymax = min((x1, x2)), max((x1, x2)), min((y1, y2)), max((y1, y2))
    # If slope is positive
    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        while xmin <= xmax and ymin <= ymax:
            point_list.append((xmin, ymin))
            xmin += 1
            ymin += 1
    # If slope is negative
    else:
        while xmin <= xmax and ymax >= ymin:
            point_list.append((xmin, ymax))
            xmin += 1
            ymax -= 1
    return point_list
    
def get_points_broad(vent):
    x1, y1, x2, y2 = vent
    axis = get_axis(vent)
    if axis == 'x':
        return get_points_narrow('x', x1, y1, y2)
    elif axis == 'y':
        return get_points_narrow('y', y1, x1, x2)
    else:
        return get_points_diag(vent)

def how_many_overlaps(point_list):
     return len(list(filter(lambda x: x[1] > 1, collections.Counter(point_list).items())))

def part_1():
    all_points = list()
    for vent in only_vert_and_horz:
        x1, y1, x2, y2 = vent
        if x1 == x2:
            local_points = get_points_narrow('x', x1, y1, y2)
        else:
            local_points = get_points_narrow('y', y1, x1, x2)
        all_points += local_points
    return how_many_overlaps(all_points)

def part_2():
    all_points = list()
    for vent in data:
        all_points += get_points_broad(vent)
    return how_many_overlaps(all_points)

if __name__ == '__main__':
    print(part_1())
    print(part_2())
