#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# Lab01_1
# 229223 Sec 002

import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = ((a+b+c)/2)
print("area:", math.ceil(math.sqrt(s*(s-a)*(s-b)*(s-c))))