#!/usr/bin/python3


def operation(argv):
    from calculator_1 import add, sub, mul, div
    import sys

    n = len(argv) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    ops = argv[2]

    if ops == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, add(a, b)))
    elif ops == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sub(a, b)))
    elif ops == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, mul(a, b)))
    elif ops == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    import sys

    operation(sys.argv)
