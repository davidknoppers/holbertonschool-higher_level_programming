#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    math_fns = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    math_symbols = ['+', '-', '*', '/']
    for i in range(4):
        print('{:d} {:s} {:d} = {:d}'.format(a, math_symbols[i], b,
                                             (math_fns[i])))
