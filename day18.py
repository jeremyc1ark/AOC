import re
from operator import add, mul, sub, truediv

def make_ops(line):
    line = re.findall(r'\d+|\(|\)|\*|\+', line)
    line = [int(x) if x.isnumeric() else x for x in line]
    return line

data = open('input.txt').read().strip().split('\n')
data = [make_ops(line) for line in data]

opp_ref = {'*': mul, '-': sub, '/': truediv, '+': add}

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
    else:
        return eval_ops(expr, acc, i+1, opp_ref[val])

def part_1(ops):
    return sum((eval_ops(expr) for expr in ops))
