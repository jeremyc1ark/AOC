from itertools import combinations_with_replacement

data = open('input.txt', 'r').read().strip('\n').split('\n')

height = len(data)
width = len(data[0])

def energy_boost(octo_map):
    return [map(lambda x: x + 1, y) for y in octo_map]

def get_adj_coords(x, y):
    possible_coords = combinations_with_replacement([-1,1,0], 2)
    possible_coords.remove((0,0))

    def coord_in_bounds(coord):
        new_x = x + coord[0]
        new_y = y + coord[1]
        return 0 < new_x < width and 0 < new_y < height

    return list(filter(coord_in_bounds, possible_coords))

def flash_coord(x, y, octo_map, flash_counter):
    octo_map[y][x] = 0
    flash_counter[y][x] = 1
    for coord in get_adj_coords(x, y):
        adj_x, adj_y = coord
        octo_map[adj_y][adj_x] += 1
    return (octo_map, flash_counter)

def get_flash_coords(octo_map, flash_counter):
    flash_coords = list()
    for i in height:
        for j in width:
            octo = octo_map[i][j]
            count = flash_counter[i][j]
            if octo > 9 and count != 0:
                flash_coords.append((j, i))
    return flash_coords

def flash_cycle(octo_map, flash_counter, flash_coords):
    for coord in flash_coords:
        octo_map, flash_counter = flash_coord(*coord, octo_map, flash_counter)
    return octo_map, flash_counter

flash_counter_initial=[[0]*width]*height

def chain_reaction(octo_map):
    flash_coords = get_flash_coords(octo_map, flash_counter_initial)
    step_counter = 0
    while flash_coords:
        octo_map, flash_counter = flash_cycle(octo_map, flash_counter, flash_coords)
        flash_coords = get_flash_coords(octo_map, flash_counter)
        step_counter += 1
    return step_counter



            