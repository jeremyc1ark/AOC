import re
import math
import numpy as np
import itertools as it
from functools import reduce
from collections import namedtuple

def parse_rule_line(line):
    range_pairs = re.findall(r'(\d+)-(\d+)', line)
    range_pair_to_range = lambda x: range(int(x[0]), int(x[1]) + 1)
    key = re.match(r'^[\w\s]+', line).group()
    rule_ranges = list(map(range_pair_to_range, range_pairs))
    return (key, rule_ranges)

data = open('input.txt', 'r').read().strip().split('\n\n')
data = list(map(lambda x: x.split('\n'), data))
tix_rules = dict(map(parse_rule_line, data[0]))
my_tik = list(map(int, data[1][1].split(',')))
near_tix = list(map(lambda x: list(map(int, x.split(','))), data[2][1:]))
data_collection = namedtuple('data_collection', 'rules, my_tik, tickets')
data = data_collection(tix_rules, my_tik, near_tix)

def get_all_ranges(rules):
    return set(it.chain.from_iterable(it.chain.from_iterable(rules.values())))

def get_all_nums(tickets):
    return list(it.chain.from_iterable(tickets))

def is_invalid_num(num, ranges):
    return num not in ranges

def part_1(ticket_info):
    all_ranges = get_all_ranges(ticket_info.rules)
    all_nums = get_all_nums(ticket_info.tickets)
    return sum(filter(lambda x: is_invalid_num(x, all_ranges), all_nums))

def is_valid_ticket(ticket, all_ranges):
    return all(map(lambda x: not is_invalid_num(x, all_ranges), ticket))

def get_all_valid_tickets(tickets, all_ranges):
    return [x for x in tickets if is_valid_ticket(x, all_ranges)]

def organize_tickets_by_common_position(tickets):
    return np.transpose(np.array(tickets))

def find_valid_fields(ticket_position, rules):
    fields = set()
    for key, ranges in rules.items():
        if all(x in ranges[0] or x in ranges[1] for x in ticket_position):
            fields.add(key)
    return fields

def make_tik_fields_list(ticket_positions, rules, my_tik):
    tik_fields_list = list()
    for i, ticket_position in enumerate(ticket_positions):
        valid_fields = find_valid_fields(ticket_position, rules)
        tik_fields_list.append([valid_fields, my_tik[i]])
    return tik_fields_list

def narrow(tik_fields_list):
    tik_fields_list.sort(key=lambda x: len(x[0]))
    key_sets, values = [list(a) for a in zip(*tik_fields_list)]
    for i, key_set in enumerate(key_sets):
        key_for_removal = list(key_set)[0]
        key_sets[i] = key_for_removal
        for elem in key_sets:
            if isinstance(elem, set):
                elem.discard(key_for_removal)
    return dict(zip(key_sets, values))

def part_2(ticket_info):
    all_ranges = get_all_ranges(ticket_info.rules)
    tickets = get_all_valid_tickets(ticket_info.tickets, all_ranges)
    positions = organize_tickets_by_common_position(tickets)
    tik_fields_list = make_tik_fields_list(positions,
                                           ticket_info.rules,
                                           ticket_info.my_tik)
    def get_departures(dict_item):
        key, val = dict_item
        return val if key.startswith('departure') else 1

    return math.prod(map(get_departures, narrow(tik_fields_list).items()))

