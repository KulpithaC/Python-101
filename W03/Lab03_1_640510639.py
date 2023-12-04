#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab04_1
# 229223 Sec 002
import math


# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()

def main():
    x1, y1, r1 = [float(x) for x in input().split()]
    x2, y2, r2 = [float(x) for x in input().split()]
    print(circle_intersect(x1, y1, r1, x2, y2, r2))

def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r = r1+r2
    if(math.isclose(d, r, abs_tol=epsilon)):
        result = 0
    elif(d < r):
        result = 1
    else:
        result = -1
    return result

def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()