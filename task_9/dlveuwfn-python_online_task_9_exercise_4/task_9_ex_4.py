"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string
from functools import reduce


def chars_in_all(*strings) -> set:
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError

    return set(reduce(set.intersection, map(set, strings)))


def chars_in_one(*strings) -> set:
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError

    return set(reduce(set.union, map(set, strings)))


def chars_in_two(*strings) -> set:
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError
    if len(strings) < 2:
        raise ValueError

    my_dict = {}
    for c in ''.join(strings):
        if c in my_dict and c.isalpha():
            my_dict[c] += 1
        elif c.isalpha():
            my_dict[c] = 1
    return {c for c in my_dict if my_dict[c] > 1}


def not_used_chars(*strings) -> set:
    if not all([isinstance(i, str) for i in strings]):
        raise TypeError

    return set(string.ascii_lowercase).difference(set(''.join(strings)))
