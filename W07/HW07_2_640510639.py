#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW07_2
# 229223 Sec 002

def main():
    assert medal_allocation(['1', '2', '3', '3', '3'])

def medal_allocation(list_a):
    gold = max(list_a)
    goldchk = list_a.count(gold)
    list_a = list(filter(lambda x: x not in gold, list_a))
    if(goldchk >= 3):
        result = tuple(map(lambda _: [gold] * goldchk, range(1)))
        result += tuple([[]] + [[]])
    silver = max(list_a)
    silverchk = list_a.count(silver)
    list_a = list(filter(lambda x: x not in silver, list_a))
    print(result)
    return result


if __name__ == '__main__':
    main()