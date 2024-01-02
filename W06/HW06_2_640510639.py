#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW06_2
# 229223 Sec 002

def main():
    nums = [1,2,3,4]
    n = -2
    print(dest_rotate_list(nums, n))  

def dest_rotate_list(list_a, n):
    len_a = len(list_a)
    n = n % len_a
    list_a[:] = (list_a[-n:] + list_a[:-n])


if __name__ == '__main__':
    main()