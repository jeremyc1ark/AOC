from copy import deepcopy
from functools import reduce

import operator as op
import numpy as np
import re

data = open('input.txt', 'r').read().strip('\n').split('\n\n')
bingo_subsystem = [int(x) for x in data[0].split(',')]

def make_bingo_row(row):
    bingo_row = re.split('\s+', row.strip())
    return [np.int32(x) for x in bingo_row]

def make_bingo_board(bingo_board_str):
    board = bingo_board_str.split('\n')
    board = [make_bingo_row(x) for x in board]
    return np.array(board, np.int32)

bingo_boards = [make_bingo_board(x) for x in data[1:]]
bingo_board_length = len(bingo_boards[0][0])
bingo_board_shape = (bingo_board_length, bingo_board_length)
no_marks = np.zeros(bingo_board_shape)
bingo_board_markings = [deepcopy(no_marks) for x in range(len(data[1:]))]

def winning_board_score(board, board_marking, most_recent_call):
    unmarked_indices = np.argwhere(board_marking == 0)
    unmarked_numbers = [board[index[0], index[1]] for index in unmarked_indices]
    return np.sum(unmarked_numbers) * most_recent_call

def has_board_won(board_marking):
    rows_and_columns = np.concatenate((board_marking, board_marking.T), axis=0)
    for elem in rows_and_columns:
        if reduce(op.mul, elem):
            return True
    return False

def mark_board(board, board_marking, call):
    board_marking_copy = deepcopy(board_marking)
    indices_to_mark = np.argwhere(board == call)
    for index in indices_to_mark:
        board_marking_copy[index[0], index[1]] = 1
    return board_marking_copy

def part_1():
    internal_board_markings = deepcopy(bingo_board_markings)
    internal_bingo_boards = deepcopy(bingo_boards)
    for call in bingo_subsystem:
        for i, board in enumerate(internal_bingo_boards):
            board_marking = internal_board_markings[i]
            new_board_marking = mark_board(board, board_marking, call)
            internal_board_markings[i] = new_board_marking
            if has_board_won(new_board_marking):
                return winning_board_score(board, new_board_marking, call)

    return "None of the boards ever won."

def eliminate_boards(indices, markings, boards):
    new_markings, new_boards = list(), list()
    for marking, board, i in zip(markings, boards, range(len(markings))):
        if i not in indices:
            new_markings.append(marking)
            new_boards.append(board)
    return new_markings, new_boards

def part_2():
    internal_board_markings = deepcopy(bingo_board_markings)
    internal_bingo_boards = deepcopy(bingo_boards)
    for call_number, call in enumerate(bingo_subsystem):
        eliminated_board_indices = list()
        for i, board in enumerate(internal_bingo_boards):
            board_marking = internal_board_markings[i]
            new_board_marking = mark_board(board, board_marking, call)
            if has_board_won(new_board_marking):
                eliminated_board_indices.append(i)
            else:
                internal_board_markings[i] = new_board_marking
        internal_board_markings, internal_bingo_boards = eliminate_boards(eliminated_board_indices, internal_board_markings, internal_bingo_boards)
        eliminated_board_indices = list()
        if len(internal_bingo_boards) == 1:
            board_marking = internal_board_markings[0]
            board = internal_bingo_boards[0]
            for c in bingo_subsystem[call_number:]:
                board_marking = mark_board(board, board_marking, c)
                if has_board_won(board_marking):
                    return winning_board_score(board, board_marking, c)     

if __name__ == '__main__':
    print(part_1())
    print(part_2())
