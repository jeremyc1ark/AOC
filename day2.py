import re

def parse(entry):
    elements = re.split('\s', entry)
    lo, hi = re.match(r'(\d+)\-(\d+)', elements[0]).groups()
    output = {
        'lo': int(lo),
        'hi': int(hi),
        'char': elements[1][0],
        'pswrd': elements[2]
    }
    return output


def part_1(data_dicts):
    def is_valid_pswrd(entry):
        char_str = re.split(f"[^{entry['char']}]", entry['pswrd'])
        char_str = ''.join(char_str)
        return entry['lo'] <= len(char_str) <= entry['hi']
    return len(list(filter(is_valid_pswrd, data_dicts)))

def part_2(data_dicts):
    def is_valid_pswrd(entry):
        pswrd = entry['pswrd']
        char = entry['char']
        first_match = pswrd[entry['lo'] - 1] == char
        second_match = pswrd[entry['hi'] - 1] == char
        return first_match != second_match
    return len(list(filter(is_valid_pswrd, data_dicts)))

if __name__ == '__main__':
    data = open('input.txt', 'r').read().split('\n')
    data = map(parse, data[0:-1])

    print(f"Answer for Part 1: {part_1(data)}")
    print(f"Answer for Part 2: {part_2(data)}")
