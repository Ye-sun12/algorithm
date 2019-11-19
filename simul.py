import argparse
import copy
import random
import timeit
import sys

from bubble import bubble_sort
from insert import insertion_sort
from selectt import selection_sort
from quick import quick_sort
from merge import merge_sort
from heap import heap_sort
from python_sort import python_sort


def generate(n, method):
    if method == "ASC":
        return list(range(n))
    elif method == "DESC":
        return list(range(n, 0, -1))
    else:
        return random.sample(range(n), n)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)   # Quick sort에서 재귀가 너무 많이 일어날 경우에 대한 대비

    # 명령행 인수를 받아서 처리할 수 있도록
    parser = argparse.ArgumentParser("Benchmark for sort algorithms")
    parser.add_argument("-n",default = 3000, type=int, help="number of data")
    parser.add_argument('-m', default='ASC',
                        choices=['ASC', 'DESC', 'RANDOM'], help="method for data generation")
    args = parser.parse_args()
    print(args)
    data = generate(args.n, args.m)
    if len(data) < 30:
        print("Data: ", data)
    algorithms = [insertion_sort, selection_sort, bubble_sort,
                  quick_sort, merge_sort, heap_sort, python_sort]
    for sort in algorithms:
        if len(data) > 10000 and sort.__name__ in ('insertion_sort', 'selection_sort', 'bubble_sort'):
            continue
        d = copy.deepcopy(data)
        print(sort.__name__, end=":\t")
        print("%.3f" %
              timeit.timeit(
                  'sort(d)', 'from __main__ import sort, d', number=1))
        if len(d) < 30:
            print(d)

        if sorted(data) != d:
            print("something wrong")
