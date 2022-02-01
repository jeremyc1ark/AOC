import collections
from copy import copy

data = open('input.txt', 'r').read().strip('\n').split(',')
data = [int(x) for x in data]

def make_age_dict(age_list):
    return dict(collections.Counter(age_list))

def one_cycle(age_dict):
    new_age_dict = dict()
    resets = 0
    for age in range(9):
        if age == 0:
            new_age_dict[8] = age_dict.get(0, 0)
            resets += age_dict.get(0, 0)
        else:
            new_age_dict[age-1] = age_dict.get(age, 0)
    new_age_dict[6] += resets
    return new_age_dict

def age_dict_to_population(age_dict):
    return sum(list(age_dict.values()))

def get_population_after(days):
    age_dict = make_age_dict(data)
    for i in range(days):
        age_dict = one_cycle(age_dict)
    return age_dict_to_population(age_dict)
        
def part_1():
    return get_population_after(18)

def part_2():
    return get_population_after(256)

if __name__ == '__main__':
    print(part_1())
    print(part_2())