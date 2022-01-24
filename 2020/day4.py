import re
import inspect

def part_1(input_data):
    def is_valid(entry):
        required_credentials = {'byr', 'hcl', 'ecl', 'iyr', 'hgt', 'pid', 'eyr'}
        overlap = required_credentials.intersection(set(entry.keys()))
        return len(required_credentials) == len(overlap)

    input_data = list(filter(is_valid, input_data))
    return len(input_data)

class ValidCreds:
    def byr(val):
        return 1920 <= int(val) <= 2002

    def iyr(val):
        return 2010 <= int(val) <= 2020

    def eyr(val):
        return 2020 <= int(val) <= 2030

    def hgt(val):
        regex_str = r"(?P<num>\d+)(?P<unit>cm|in)"
        match = re.match(regex_str, val)
        if match is None:
            return False
        reqs = {'cm': {'lo': 150, 'hi': 193},
                'in': {'lo': 59, 'hi': 76}}
        match_dict = match.groupdict()
        val_range = reqs[match_dict['unit']]
        return val_range['lo'] <= int(match_dict['num']) <= val_range['hi']

    def hcl(val):
        return bool(re.match(r"#[0-9a-f]{6}", val))

    def ecl(val):
        return val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    def pid(val):
        return bool(re.match(r"^\d{9}$", val))

def part_2(input_data):
    req_dict = dict(inspect.getmembers(ValidCreds, predicate=inspect.isfunction))
    req_creds = list(req_dict.keys())
    def is_valid(entry, req, reqs):
        entry_val = entry.get(req, False)
        if not entry_val:
            return False
        elif not reqs:
            return req_dict[req](entry_val)
        elif req_dict[req](entry_val):
            return is_valid(entry, reqs[0], reqs[1:])
        else:
            return False
    return len(list(filter(lambda x: is_valid(x, req_creds[0], req_creds[1:]), input_data)))

if __name__ == '__main__':
    data = open('input.txt', 'r').read().split('\n\n')
    data = map(lambda x:
            map(lambda b: b.split(':'),
                re.split(r'\s|\n', x)),
            data)
    data = map(lambda x: filter(lambda y: len(y) == 2, x), data)
    data = list(map(dict, data))

    print(f"Answer for Part 1: {part_1(data)}")
    print(f"Answer for Part 2: {part_2(data)}")
