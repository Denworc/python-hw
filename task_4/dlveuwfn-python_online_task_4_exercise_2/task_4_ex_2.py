"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError()
    test_string = ''.join(elem.lower() for elem in test_string if elem.isalnum())
    if len(test_string) > 1:
        for index in range(len(test_string) // 2):
            if test_string[index] != test_string[-index - 1]:
                return False
    return True
