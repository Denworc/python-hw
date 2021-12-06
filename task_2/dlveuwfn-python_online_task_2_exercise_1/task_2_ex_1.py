"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int, help="capacity of a knapsack")
parser.add_argument("-w", nargs="+", type=int, help="list of weights")
parser.add_argument("-n", type=int, help="number of gold bars")


def input_check(args):
    if len(args.w) != args.n:
        raise ValueError("")
    if args.W < 0 or args.n < 0:
        raise ValueError("")
    for elem in args.w:
        if elem < 0:
            raise ValueError("")


def bounded_knapsack(args):
    max_capacity = args.W
    weights = args.w
    capacity_range = [1] + [0] * max_capacity

    for weight in weights:
        for i in range(max_capacity, weight - 1, -1):
            if capacity_range[i - weight] == 1:
                capacity_range[i] = 1
    i = max_capacity
    while capacity_range[i] == 0:
        i -= 1
    return i


def main():
    args = parser.parse_args()
    input_check(args)
    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
