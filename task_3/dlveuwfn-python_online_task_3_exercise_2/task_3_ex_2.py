"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("numerals", type=str, help="Roman numeral")


def from_roman_numerals(args):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    roman_numeral = args.numerals
    for elem in roman_numeral:
        if elem not in roman.keys():
            raise ValueError()

    result = 0
    prev_val = 0
    for index, value in enumerate(roman_numeral):
        if index > 0 and roman[value] > prev_val:
            result += roman[value] - 2 * prev_val
        else:
            result += roman[value]
        prev_val = roman[value]
    return result


def main():
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
