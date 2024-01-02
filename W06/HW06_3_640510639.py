#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW06_3
# 229223 Sec 002
from functools import reduce

def main():
    assert moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

def moving_average(list_a, w):
    count_list = lambda x, y: x + [x[-1] + y] if x else [y]
    reduce_list = reduce(count_list, list_a, [])
    average = lambda i: reduce_list[i] / w if i < w else (reduce_list[i] - reduce_list[i - w]) / w
    result = list(map(average, range(w - 1, len(list_a))))
    return result


if __name__ == '__main__':
    main()