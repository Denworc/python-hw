""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse

parser = argparse.ArgumentParser(description="Perform EBNF formula")
parser.add_argument("user_input", type=str, help="EBNF formula")


def operate(result, number, operator):
    if operator == "+":
        return result + number
    elif operator == "-":
        return result - number
    return number


def check_formula(user_input):
    number = None
    result = None
    operator = 0

    if not user_input:
        return False, None

    for elem in user_input:
        if elem.isdigit():
            if number is None:
                number = 0
            number = number * 10 + int(elem)
        elif elem in "+-":
            if number is None:
                return False, None
            result = operate(result, number, operator)
            operator = elem
            number = None
        else:
            return False, None
    if number:
        return True, operate(result, number, operator)
    return False, None


def main():
    args = parser.parse_args()
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
