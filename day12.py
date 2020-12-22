import math

data = open('input.txt', 'r').read().strip().split('\n')
data = list(map(lambda x: (x[0], int(x[1:])), data))


def part_1(input_data):
    horz, vert = 0, 0
    angle = 0

    opp_dict = {
        'F': lambda arg: (math.cos(math.radians(angle)) * arg + horz,
             math.sin(math.radians(angle)) * arg + vert, angle),
        'R': lambda arg: (horz, vert, angle - arg),
        'L': lambda arg: (horz, vert, angle + arg),
        'N': lambda arg: (horz, vert + arg, angle),
        'S': lambda arg: (horz, vert - arg, angle),
        'E': lambda arg: (horz + arg, vert, angle),
        'W': lambda arg: (horz - arg, vert, angle)}

    for opp, arg in input_data:
        horz, vert, angle = opp_dict[opp](arg)
    return int(abs(horz) + abs(vert))


def part_2(input_data):
    horz, vert = 0, 0
    x, y = 10, 1

    def rotate(x,y,degrees):
        rads = math.radians(degrees)
        c = math.cos(rads)
        s = math.sin(rads)
        return (int(x * c - y * s), int(x * s + y * c))

    opp_dict = {
        'F': lambda a: (arg * x + horz, arg * y + vert, x, y),
        'R': lambda a: (horz, vert, *rotate(x, y, -arg)),
        'L': lambda a: (horz, vert, *rotate(x, y, arg)),
        'N': lambda a: (horz, vert, x, y + arg),
        'S': lambda a: (horz, vert, x, y - arg),
        'E': lambda a: (horz, vert, x + arg, y),
        'W': lambda a: (horz, vert, x - arg, y)}

    for opp, arg in input_data:
        horz, vert, x, y = opp_dict[opp](arg)
        print(horz, vert, x, y, opp, arg)

    return abs(horz) + abs(vert)

