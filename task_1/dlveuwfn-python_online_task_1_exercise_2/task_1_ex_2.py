"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import math
import operator

parser = argparse.ArgumentParser(description="Perform standard math functions")
parser.add_argument("func", type=str, help="math function")
parser.add_argument("operand1", type=float, help="first operand")
parser.add_argument("operand2", nargs="?", type=float, default=None, help="second operand")


def calculate(args):
    operand1 = args.operand1
    operand2 = args.operand2
    func = args.func

    if operation := getattr(math, func, None) or getattr(operator, func, None):
        return float(operation(operand1, operand2) if operand2 else operation(operand1))
    raise NotImplementedError(f"passed operation {func} not implemented!")


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
