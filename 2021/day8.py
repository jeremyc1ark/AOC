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

lighting_ref = [
    {0,1,2,4,5,6},
    {2,5},
    {0,2,3,4,6},
    {0,2,3,5,6},
    {1,2,3,5},
    {0,1,3,5,6},
    {0,1,3,4,5,6},
    {0,2,5},
    {0,1,2,3,4,5,6},
    {0,1,2,3,5}
]

def get_easy_digits(patterns):
    digits_to_patterns = dict()
    lens_to_digits = {2:1, 3:7, 4:4, 7:8}
    for pattern in patterns:
        digit = lens_to_digits.get(len(pattern), False)
        if digit:
            digits_to_patterns[digit] = pattern
    return digits_to_patterns

all_char_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

# This is a disgusting piece of code :/
# Need a generic soln rather than brute force
def solve_segments(patterns):
    # Segment numbers To Letters
    ntl = dict()
    known_digits = get_easy_digits(patterns)
    # Solving for segment 0
    ntl[0] = known_digits[7].difference(known_digits[1])
    # Finding the string set for digits 6 and 0
    for pattern in patterns:
        print(pattern)
        if len(pattern) == 6:
            print('hello')
            if len(pattern.difference(all_char_set).intersection(known_digits[1])) == 1:
                
                known_digits[6] = pattern
            else:
                known_digits[0] = pattern
    # Solving for segment 2
    ntl[2] = all_char_set.difference(known_digits[6])
    # Solving for segment 5
    ntl[5] = known_digits[7].difference({ntl[0], ntl[2]})
    # Solving for segment 3
    ntl[3] = known_digits[8].difference(known_digits[0])
    # Finding the string set for digits 3, solving for segment 6
    for pattern in patterns:
        if len(pattern) == 5:
            diff = pattern.difference({ntl[x] for x in [0,2,3,5]})
            if len(diff) == 1:
                known_digits[3] = pattern
                ntl[6] = diff
    # Solving for segments 1 and 4
    one_and_four = known_digits[8].difference(known_digits[3])
    ntl[1] = one_and_four.intersection(known_digits[4])
    ntl[4] = one_and_four.difference(ntl[1])

    # Removing set wrappers
    for i in range(7):
        ntl[i] = list(ntl[i])[0]
    return ntl



    

if __name__ == '__main__':
    print(part_1())
    sample = [set(word) for word in "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")]
    print(solve_segments(sample))
    
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
    
    