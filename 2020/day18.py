import re
import math
from operator import add, mul

def make_ops(line):
    line = re.findall(r'\d+|\(|\)|\*|\+', line)
    line = [int(x) if x.isnumeric() else x for x in line]
    return line

data = open('input.txt').read().strip().split('\n')
data = [make_ops(line) for line in data]


def cp_index(i, lat, o=1, c=0):
    # Stands for Closing Paren. Finds index of
    # corresponding paren
    if o != c:
        if i == len(lat):
            return i - 1
        elif lat[i] == '(':
            return cp_index(i+1, lat, o+1, c)
        elif lat[i] == ')':
            return cp_index(i+1, lat, o, c+1)
        else:
            return cp_index(i+1, lat, o, c)
    return i - 1


def part_1(ops):
    op_dict = {'+': add, '*': mul}
    def null_op(a, b):
        return b
    def eval_ops(expr, acc=0, i=0, opp=null_op):
        if i == len(expr):
            return acc
        val = expr[i]
        if val == '(':
            cpi = cp_index(i+1, expr)
            next_term = eval_ops(expr[i+1:cpi])
            return eval_ops(expr, opp(acc, next_term), cpi+1, None)
        elif val == ')':
            return acc
        elif isinstance(val, int):
            return eval_ops(expr, opp(acc, val), i+1, None)
        elif val in '*+':
            return eval_ops(expr, acc, i+1, op_dict[val])
        else:
            print("Error: Unknown symbol")
            return None
    return sum((eval_ops(expr) for expr in ops))


def part_2(ops):
    def eval_ops(expr, i, total_acc, region_acc):
        # Been having difficulties with using default arguments in
        # recursion, so we're just using positionals.
        if i == len(expr):
            return math.prod(total_acc) * region_acc
        val = expr[i]
        if val == '*':
            total_acc.append(region_acc)
            return eval_ops(expr, i+1, total_acc, 0)
        elif val == '+':
            return eval_ops(expr, i+1, total_acc, region_acc)
        elif isinstance(val, int):
            return eval_ops(expr, i+1, total_acc, region_acc+val)
        elif val == '(':
            cpi = cp_index(i+1, expr)
            term = eval_ops(expr[i+1:cpi], 0, list(), 0)
            return eval_ops(expr, cpi+1, total_acc, region_acc+term)
        else:
            print("Error: Unknown symbol")
            return None
    return sum((eval_ops(expr, 0, list(), 0) for expr in ops))
