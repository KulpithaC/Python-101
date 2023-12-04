#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab03_2
# 229223 Sec 002
import math


# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function is_p_triple()

def main():
    x, y, z = [int(x) for x in input().split()]
    print(is_p_triple(x, y ,z))


def is_p_triple(x, y, z):
    if((math.sqrt(x**2 + y**2) == z) or (math.sqrt(x**2 + z**2) == y) or (math.sqrt(y**2 + z**2) == x)):
        return True
    return False

def test_p_triple():
    assert is_p_triple(4, 5, 3) == True
    assert is_p_triple(42, 9, 41) == False
    print("all ok!")


if __name__ == '__main__':
    main()