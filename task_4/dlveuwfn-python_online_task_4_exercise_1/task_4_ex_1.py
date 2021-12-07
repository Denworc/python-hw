"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    new_string = ""
    for elem in string:
        if elem == "\"":
            new_string += "\'"
        elif elem == "\'":
            new_string += "\""
        else:
            new_string += elem
    return new_string