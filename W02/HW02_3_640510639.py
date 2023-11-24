#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW02_3
# 229223 Sec 002
import math

def main():
    number = int(input())
    k = int(input())
    value = int(input())
    result = set_kth_digit(number, k, value)
    print(result)

def kth_digit(number, k):
    result = abs(number)//10**(k)%10
    return result

def set_kth_digit(number, k, value):
    result = number - (kth_digit(number, k) * 10 ** k) + (value * 10 ** k)
    return result

if __name__ == '__main__':
    main()
