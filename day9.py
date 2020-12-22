from itertools import combinations

data = open('input.txt', 'r').read().strip().split('\n')
data = list(map(int, data))

def part_1(input_data, index=25):
    current = input_data[index]
    preamble = input_data[index-25:index]
    combos = combinations(preamble, 2)
    for combo in combos:
        if sum(combo) == current:
            return part_1(input_data, index+1)
    return current

def part_2(input_data):
    target_num = part_1(input_data, index=25)

    def helper(index=0, prevs=[]):
        prevs.append(input_data[index])
        while sum(prevs) > target_num:
            prevs = prevs[1:]
        if sum(prevs) == target_num and len(prevs) > 1:
            return min(prevs) + max(prevs)
        return helper(index+1, prevs)

    return helper()
