import numpy as np
import operator as op
import math

data = open('input.txt', 'r').read().strip('\n').split('\n')
data = list(map(lambda x: list(map(int, list(x.strip()))), data))
data = np.array(data, np.int32)
transposed_data = data.T

def power_consumption(gamma, epsilon):
    return gamma*epsilon

def get_bit(column, greek_letter):
    if greek_letter == 'gamma':
        return int(sum(column) > math.floor(len(column)/2))
    elif greek_letter == 'epsilon':
        return int(sum(column) < math.floor(len(column)/2))

def get_byte_in_dec(transposed_data, greek_letter):
    bit_list = list(map(lambda column: get_bit(column, greek_letter), transposed_data))
    bit_list = [str(x) for x in bit_list]
    byte = ''.join(bit_list)
    return int(byte, base=2)


def part_1():
    gamma = get_byte_in_dec(transposed_data, 'gamma')
    epsilon = get_byte_in_dec(transposed_data, 'epsilon')   
    return power_consumption(gamma, epsilon)

def most_common_bit(bit_list, type):
    rating_dict = {
        'carbon': op.lt,
        'oxygen': op.ge
    }
    return int(rating_dict[type](sum(bit_list), len(bit_list)/2))

def generic_rating(type):
    # Get abstracted, boi.
    
    def helper(remaining_bytes, i=0):
        current_column = remaining_bytes[:, i]
        most_common = most_common_bit(current_column, type)
        remaining_bytes = np.array(list(filter(lambda x: x[i] == most_common, remaining_bytes)), np.int32)
        if len(remaining_bytes) == 1:
            return int(''.join([str(x) for x in remaining_bytes[0]]), base=2)         
        else:
            return generic_rating(type)(remaining_bytes, i+1)

    return helper

carbon_rating = generic_rating('carbon')
oxygen_rating = generic_rating('oxygen')

def part_2():
    return carbon_rating(data) * oxygen_rating(data)

if __name__ == '__main__':
    print(part_1())
    print(part_2())