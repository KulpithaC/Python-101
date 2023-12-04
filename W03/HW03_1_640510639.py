#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_1
# 229223 Sec 002

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_min_mid_max(a, b, c)
    

def my_min_mid_max(a, b, c):
    if(a > b):
       max_ = a
       min_ = b
    else:
       max_ = b
       min_ = a

    if(c > max_):
       mid = max_
       max_ = c
    else:
        if(c < min_):
            mid = min_
            min_ = c
        else:
            mid = c
    print("min =", min_, "\nmid =", mid, "\nmax =", max_)
    return 0

if __name__ == '__main__':
    main()