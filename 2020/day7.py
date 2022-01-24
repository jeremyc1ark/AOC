import re
from collections import defaultdict, namedtuple

data = open('input.txt', 'r').read().strip().split('\n')

def part_1(input_data, target_bag):
    def take_line(line):
        subject = re.match(r'\w+\s\w+', line).group()
        regex_str = r'\s?\d+\s(\w+\s\w+)'
        bag_list = re.findall(regex_str, line)
        return (subject, bag_list)
    bag_dict = defaultdict(list)
    for line in input_data:
        subject, bag_list = take_line(line)
        for bag in bag_list:
            bag_dict[bag].append(subject)
    def helper(bag, bag_set=set()):
        if not bag_dict[bag]:
            return bag_set
        def recur(x):
            bag_set.add(x)
            return helper(x, bag_set)
        return set.union(*map(recur, bag_dict[bag]))
    return len(helper(target_bag))


def part_2(input_data, target_bag):
    def take_line(line):
        subject = re.match(r'\w+\s\w+', line).group()
        regex_str = r'\s?(?P<quantity>\d+)\s(?P<name>\w+\s\w+)'
        BagPair = namedtuple('BagPair', ['name', 'quantity'])
        bag_list = list(map(lambda x: BagPair(x.group('name'), int(x.group('quantity'))),
                        re.finditer(regex_str, line)))
        return (subject, bag_list)
    bag_dict = dict(map(take_line, input_data))
    def helper(key):
        new_bag = bag_dict.get(key, False)
        if new_bag:
            return sum(map(lambda x: x.quantity * (1 + helper(x.name)), new_bag))
        return 0
    return helper(target_bag)
