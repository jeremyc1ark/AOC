import re
from copy import copy
import itertools as it
from collections import namedtuple

parse_mem_pair = lambda x: tuple(map(int, re.match(r'mem\[(\d+)\]\s=\s(\d+)', x).groups()))
parse_mask = lambda x: re.match(r'mask\s=\s([\d\w]+)', x).group(1)
parse_entry = lambda y: parse_mem_pair(y) if re.match(r'mem', y) else parse_mask(y)

data = open('input.txt', 'r').read().strip().split('\n')
data = list(map(parse_entry, data))

def get_val(num, mask):
    bit_str = "{:036b}".format(num)
    masker = lambda m, b: m if m != 'X' else b
    return int(''.join(map(masker, mask, bit_str)), 2)

def part_1(input_data):
    mem_pairs = dict()
    for entry in input_data:
        if isinstance(entry, str):
            mask = entry
        else:
            location, dec = entry
            mem_pairs[location] = get_val(dec, mask)
    return sum(mem_pairs.values())

def get_mem_addresses(address, mask):
    indices = list()
    def masker(m, b, i):
        if m == '0':
            return b
        elif m == '1':
            return '1'
        else:
            indices.append(i)
            return 'X'
    bit_str = "{:036b}".format(address)
    float_list = list(map(masker, mask, bit_str, range(0, 36)))
    change_templates = it.product(['1', '0'], repeat=len(indices))

    mem_addresses = list()
    for template in change_templates:
        new_float = copy(float_list)
        for index, change in enumerate(template):
            new_float[indices[index]] = change
        mem_addresses.append(''.join(new_float))
    return list(map(lambda x: int(x, 2), mem_addresses))

def part_2(input_data):
    mem_pairs = dict()
    mask = None
    for entry in input_data:
        if isinstance(entry, str):
            mask = entry
        else:
            location, dec = entry
            mem_adreses = get_mem_addresses(location, mask)
            mem_pairs.update(dict(zip(mem_adreses,
                                      [dec] * len(mem_adreses))))
    return sum(mem_pairs.values())



