import collections

data = open('input.txt', 'r').read().strip('\n').split('\n')

open_chars = set("([{<")
close_chars = set(")]}>")

open_to_close = dict(zip(tuple("([{<"), tuple(")]}>")))

penalty_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def test_line(l):
    i = 0
    stack = collections.deque()
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

        
if __name__ == '__main__':
    print(sum(map(test_line, data)))