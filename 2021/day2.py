from collections import namedtuple

data = open('input.txt', 'r').read().strip('\n').split('\n')

Coord = namedtuple('Coord', ['x', 'y'])
Line = namedtuple('Line', ['direction', 'quantity'])

def group_line(line):
    line = line.strip().split(' ')
    line[1] = int(line[1])
    return Line(*line)

data = [group_line(x) for x in data]

def create_modifier(direction, quantity):
    direction_dict = {
    'forward': Coord(1, 0),
    'down': Coord(0, 1),
    'up': Coord(0, -1)
    }
    template = direction_dict[direction]
    return Coord(template.x*quantity, template.y*quantity)

def use_modifier(current_pos, modifier):
    return Coord(current_pos.x+modifier.x, current_pos.y+modifier.y)

def part_1():
    part_1_data = [create_modifier(*x) for x in data]
    current_pos = Coord(0, 0)
    for modifier in part_1_data:
        current_pos = use_modifier(current_pos, modifier)
    return current_pos.x * current_pos.y

def part_2():
    current_pos = Coord(0, 0)
    aim = 0
    for line in data:
        if line.direction == 'up':
            aim += line.quantity
        elif line.direction == 'down':
            aim -= line.quantity
        else:
            current_pos = Coord(current_pos.x+line.quantity, current_pos.y-aim*line.quantity)
    return current_pos.x * current_pos.y

if __name__ == '__main__':
    print(part_1())
    print(part_2())