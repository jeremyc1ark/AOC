import collections

data = open('input.txt', 'r').read().strip('\n').split('\n')

correspondence_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

closing_chars = set(")]}>")

penalty_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

char_status = collections.namedtuple('char_status', ['i', 'char', 'status'])

def find_chunk_end(line, i=0):
    open_char = line[i]
    if open_char in closing_chars:
        return char_status(i, line[i], False)
    valid_closer = correspondence_dict[open_char]
    line_range = range(len(line))
    if i + 1 not in line_range:
        return char_status(i, None, False)
    if line[i+1] == valid_closer:
        return char_status(i+1, line[i+1], True)
    
    def get_to_end(i):
        end_of_internal_chunk = find_chunk_end(line, i+1)
        if end_of_internal_chunk.status:
            if end_of_internal_chunk.i + 2 in range(len(line)):
                if line[end_of_internal_chunk.i + 1] == valid_closer:
                    new_i = end_of_internal_chunk.i + 1
                    return char_status(new_i, line[new_i], True)
                else:
                    return get_to_end(end_of_internal_chunk + 1)
        else:
            return end_of_internal_chunk
    
    return get_to_end(i)


if __name__ == '__main__':
    line = "(((())"
    print(find_chunk_end(line))