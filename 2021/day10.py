from collections import deque
from functools import reduce

data = open('input.txt', 'r').read().strip('\n').split('\n')

open_chars = set("([{<")
open_to_close = dict(zip(tuple("([{<"), tuple(")]}>")))

penalty_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def test_line(l):
    i = 0
    stack = deque()
    while i < len(l):
        char = l[i]
        if char in open_chars:
            stack.append(open_to_close[char])
        else:
            if stack:
                expected_close = stack.pop()
                if char != expected_close:
                    return penalty_dict[char]
            else:
                return penalty_dict[char]
        i += 1
    return 0

def autocomplete(l):
    i = 0
    stack = deque()
    while i < len(l):
        char = l[i]
        if char in open_chars:
            stack.append(open_to_close[char])
        else:
            stack.pop()
        i += 1
    stack.reverse()
    return ''.join(stack)

points_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def line_to_score(line):
    completion = autocomplete(line)
    return reduce(lambda x, y: x * 5 + points_dict[y], completion, 0)

def get_middle(score_list):
    score_list = sorted(score_list)
    i = (len(score_list) - 1) / 2
    return score_list[int(i)]

def part_1():
    return sum(map(test_line, data))

def part_2():
    valid_lines = filter(lambda x: test_line(x) == 0, data)
    return get_middle(map(line_to_score, valid_lines))
        
if __name__ == '__main__':
    print(part_1())
    print(part_2())