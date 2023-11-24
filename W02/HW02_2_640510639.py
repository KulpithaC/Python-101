#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW02_2
# 229223 Sec 002
import math

def main():
    number = int(input(""))
    k = int(input(""))
    result = kth_digit(number, k)
    print(result)

def kth_digit(number, k):
    result = abs(number)//10**(k)%10
    return result

if __name__ == '__main__':
    main()
