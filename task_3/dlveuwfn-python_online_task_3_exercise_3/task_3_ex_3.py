"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import fnmatch
import os
import stat

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path")
parser.add_argument("-p", type=str, help="search pattern")


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    files = os.listdir(path)
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            yield os.path.join(path, name)


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    files_count = 0

    for path in file_paths:
        files_count += 1
        status = os.stat(path)
        print(path, stat.filemode(status.st_mode))
    print(f"Found {files_count} file(s).")


def main():
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()
