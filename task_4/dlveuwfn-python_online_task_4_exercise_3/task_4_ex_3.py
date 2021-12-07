"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = "") -> list:
    result_list = []
    if (not (isinstance(str_to_split, str) and isinstance(delimiter, str))) or not delimiter:
        raise ValueError()

    if not str_to_split:
        return [str_to_split]
    start = 0
    for index, char in enumerate(str_to_split):
        if char == delimiter:
            result_list.append(str_to_split[start:index])
            start = index + 1
    if start == 0:
        return [str_to_split]
    result_list.append(str_to_split[start:index + 1])

    return result_list
