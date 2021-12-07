"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


# def count_letters(given_string: str) -> dict:
#     if not isinstance(given_string, str):
#         raise TypeError
#
#     result = {}
#     for c in set(given_string):
#         if c.isalpha():
#             result[c] = given_string.count(c)
#     return result


def count_letters(given_string: str) -> dict:
    if not isinstance(given_string, str):
        raise TypeError

    result = {}
    for c in given_string:
        if c in result and c.isalpha():
            result[c] += 1
        elif c.isalpha():
            result[c] = 1
    return result
