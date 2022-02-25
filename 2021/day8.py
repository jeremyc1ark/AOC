import collections

Line = collections.namedtuple('Line', ['patterns', 'output'])
data = open('input.txt', 'r').read().strip('\n').split('\n')

def process_line(line):
    new_line = line.strip(" ").split(" | ")
    patterns = [set(pattern) for pattern in new_line[0].split(" ")]
    output = new_line[1].split(" ")
    return Line(patterns, output)

data = [process_line(line) for line in data]

def part_1():
    recognizable_numbers = 0
    for line in data:
        for output in line.output:
            if len(output) in (2, 3, 4, 7):
                recognizable_numbers += 1
    return recognizable_numbers

# Get the strings for the digits with a unique number of segments
def get_easy_digits(patterns):
    digits_to_patterns = dict()
    lens_to_digits = {2:1, 3:7, 4:4, 7:8}
    for pattern in patterns:
        digit = lens_to_digits.get(len(pattern), False)
        if digit:
            digits_to_patterns[digit] = pattern
    return digits_to_patterns

# Flipping the dictionary
def ntl_to_ltn(ntl):
    ltn = dict()
    for key, value in ntl.items():
        ltn[value] = key
    return ltn

def remove_set_wrappers(ntl):
    for i in range(7):
        ntl[i] = list(ntl[i])[0]
    return ntl_to_ltn(ntl)

"""         0
    --------
   |        |
  1|        |2
   |    3   |
   ----------
   |        |
  4|        |5
   |    6   |
   ---------- """

lighting_ref = [
    {0,1,2,4,5,6},  # 0
    {2,5},          # 1
    {0,2,3,4,6},    # 2
    {0,2,3,5,6},    # 3
    {1,2,3,5},      # 4 
    {0,1,3,5,6},    # 5
    {0,1,3,4,5,6},  # 6
    {0,2,5},        # 7
    {0,1,2,3,4,5,6},# 8
    {0,1,2,3,5,6}   # 9
]

# Get the strings of all the digits
def get_all_digit_strings(patterns):
    # Get digits that are known so far
    known_digits = get_easy_digits(patterns)

    # Solving for digit 6
    for pattern in patterns:
        if len(pattern) == 6:
            if known_digits[1].difference(pattern):
                known_digits[6] = pattern
    # Solving for digit 0 and 9
    for pattern in patterns:
        if len(pattern) == 6:
            if pattern == known_digits[6]:
                continue
            elif known_digits[4].difference(pattern):
                known_digits[0] = pattern
            else:
                known_digits[9] = pattern

    # Solving for digit 3
    for pattern in patterns:
        if len(pattern) == 5:
            if not known_digits[7].difference(pattern):
                known_digits[3] = pattern

    # Solving for digit 2
    for pattern in patterns:
        if len(pattern) == 5:
            if pattern != known_digits[3]:
                if len(known_digits[4].difference(pattern)) == 2:
                    known_digits[2] = pattern
                else:
                    known_digits[5] = pattern
    return known_digits
    
def solve_segments(patterns):
    # segment Numbers To Letters
    ntl = dict()

    # Getting the strings for all the digits
    known_digits = get_all_digit_strings(patterns)

    # Solving for segment 0
    ntl[0] = known_digits[7].difference(known_digits[1])

    # Solving for segment 2
    ntl[2] = known_digits[1].difference(known_digits[5])

    # Solving for segment 5
    ntl[5] = known_digits[1].difference(known_digits[2])

    # Solving for segment 1
    ntl[1] = known_digits[9].difference(known_digits[3])

    # Solving for segment 3
    ntl[3] = known_digits[2].difference(known_digits[0])

    # Solving for segment 4
    ntl[4] = known_digits[2].difference(known_digits[3])

    # Solving for segment 6
    known_segments = ''.join([list(x)[0] for x in ntl.values()])
    ntl[6] = set('abcdefg').difference(known_segments)

    # Removing set wrappers
    return remove_set_wrappers(ntl)            
    


def decipher_digit(key, digit_string):
    lighting = {key[char] for char in digit_string}
    for i, l in enumerate(lighting_ref):
        if lighting == l:
            return i

def decipher_line(line):
    key = solve_segments(line.patterns)
    int_list = [decipher_digit(key, string) for string in line.output]
    str_list = [str(x) for x in int_list]
    return int(''.join(str_list))

def part_2():
    return sum([decipher_line(line) for line in data])

if __name__ == '__main__':
    print(part_2())
    
    