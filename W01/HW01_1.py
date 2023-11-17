#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW01_1
# 229223 Sec 002

m1 = float(input("m1: "))
b1 = float(input("b1: "))
m2 = float(input("m2: "))
b2 = float(input("b2: "))
x = (b2 - b1)/(m1 - m2)
y = (m2 * x) + b2
print("Lines intersect at (%.2f,%.2f)" %(x,y))