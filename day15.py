from collections import namedtuple

data = open('input.txt', 'r').read().strip().split(',')
data = list(map(int, data))

def play_game(starting_nums, end_num):
    num_memory = {num : i for num, i in zip(starting_nums[:-1], range(1, len(starting_nums)))}
    record = namedtuple('record', 'num, index, is_first')
    spoken = record(starting_nums[-1], len(starting_nums), True)

    for i in range(len(starting_nums)+1, end_num+1):
        if spoken.is_first:
            new_num = 0
        else:
            new_num = spoken.index - num_memory[spoken.num]
        will_be_first = new_num not in num_memory
        num_memory[spoken.num] = spoken.index
        spoken = record(new_num, i, will_be_first)

    return spoken.num

def part_1(starting_nums):
    return play_game(starting_nums, 2020)

def part_2(starting_nums):
    return play_game(starting_nums, 30000000)

