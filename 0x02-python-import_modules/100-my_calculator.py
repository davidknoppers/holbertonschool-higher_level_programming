#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    math_fns = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    math_symbols = ['+', '-', '*', '/']

    if argv[2] not in math_symbols:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
