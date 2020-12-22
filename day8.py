import copy

data = open('input.txt', 'r').read().strip().split('\n')
data = map(lambda x: x.split(' '), data)
data = list(map(lambda x: (x[0], int(x[1])), data))

def run_prog(input_data):
    done = False
    index = 0
    acc = 0
    visited = set()

    while not done:
        opp, arg = input_data[index]

        if index in visited:
            return False, acc

        visited.add(index)

        if opp == 'jmp':
            index += arg
        elif opp == 'acc':
            acc += arg
            index += 1
        else:
            index += 1

        done = index == len(input_data)

    return True, acc

def part_1(input_data):
    return run_prog(input_data)[1]

def part_2(input_data):
    for index, line in enumerate(input_data):
        data_copy = copy.copy(input_data)
        switch = {'jmp':'nop','nop':'jmp','acc':'acc'}
        opp, arg = data_copy[index]
        data_copy[index] = (switch[opp], arg)
        ran, acc = run_prog(data_copy)
        if ran: return acc
    return False
