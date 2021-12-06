"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse

parser = argparse.ArgumentParser(description="Perform arithmetic operation")
parser.add_argument("operand1", type=float, help="first operand")
parser.add_argument("operator", type=str, help="operator ( math sign )")
parser.add_argument("operand2", type=float, help="second operand")


def calculate(args):
    operand1 = args.operand1
    operand2 = args.operand2
    operator = args.operator

    math_operations = {
        "+": lambda op1, op2: op1+op2,
        "-": lambda op1, op2: op1-op2,
        "*": lambda op1, op2: op1*op2,
        "/": lambda op1, op2: op1/op2,
    }

    if operation := math_operations.get(operator):
        return operation(operand1, operand2)
    raise NotImplementedError(f"passed operation {operator} not implemented!")


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
