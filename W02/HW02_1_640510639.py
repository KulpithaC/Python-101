#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW02_1
# 229223 Sec 002
import math

def octagon_area(x):
    area = (x*x)-(4*(1/2*x/3*x/3))
    return area

def main():
    x = int(input())
    
    print(octagon_area(x))

if __name__ == '__main__':
    main()