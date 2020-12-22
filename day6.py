data = open('input.txt', 'r').read().strip().split('\n\n')

def part_1(input_data):
    new_data = map(lambda x: len(set(x.replace('\n', ''))), input_data)
    return sum(new_data)

def all_yes(group):
    new_data = list(map(set, group.split()))
    return len(set.intersection(*new_data))

def part_2(input_data):
    return sum(map(all_yes, input_data))
