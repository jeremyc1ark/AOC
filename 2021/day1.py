data = open('input.txt', 'r').read().split('\n')
data = [int(x) for x in data]

def was_there_increase(data_pair):
    prev, x = data_pair
    return x > prev
        
def make_data_tuple(i, window_size, input):
    return [input[i+x] for x in range(window_size)]

def make_data_tuples(window_size, input):
    return list(map(lambda x: make_data_tuple(x, window_size, input), range(len(input)-window_size+1)))

def part_1():
    return sum(map(was_there_increase, make_data_tuples(2, data)))

def part_2():
    three_sliding_window = list(map(sum, list(make_data_tuples(3, data))))
    return sum(map(was_there_increase, make_data_tuples(2, three_sliding_window)))


if __name__ == '__main__':
    print(part_1())
    print(part_2())

