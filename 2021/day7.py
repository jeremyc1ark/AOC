data = open('input.txt', 'r').read().strip('\n').split(',')
data = [int(x) for x in data]

def one_sub_fuel_human(pos, destination):
    return abs(pos - destination)

def one_sub_fuel_crab(pos, destination):
    diff = one_sub_fuel_human(pos, destination)
    return int((diff * (diff + 1)) / 2)

def total_fuel(pos_list, destination, engineer):
    if engineer == 'human':
        fuel_func = one_sub_fuel_human
    elif engineer == 'crab':
        fuel_func = one_sub_fuel_crab
    return sum([fuel_func(pos, destination) for pos in pos_list])


def get_least_fuel(engineer):
    min_pos = min(data)
    max_pos = max(data)
    least_fuel = 10 ** 100
    current_destination = min_pos
    while current_destination <= max_pos:
        fuel_at_current_destination = total_fuel(data, current_destination, engineer)
        if fuel_at_current_destination < least_fuel:
            least_fuel = fuel_at_current_destination
        current_destination += 1
    return least_fuel

def part_1():
    return get_least_fuel('human')

def part_2():
    return get_least_fuel('crab')

if __name__ == '__main__':
    print(part_1())
    print(part_2())
    
        