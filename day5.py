data = open('input.txt', 'r').read().split('\n')[:-1]

def get_id(partition):
    replace_dict = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    for key, val in replace_dict.items():
        partition = partition.replace(key, val)
    return int(partition, 2)

def part_1(input_data):
    return max(map(get_id, input_data))

def part_2(input_data):
    all_ids = list(map(get_id, input_data))
    lo, hi = min(all_ids), max(all_ids)
    id_range = ((hi * (hi + 1)) / 2) - ((lo * (lo - 1)) / 2)
    return int(id_range - sum(all_ids))
