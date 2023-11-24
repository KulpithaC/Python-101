#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Lab02_2
# 229223 Sec 002
import math

def main():
    x = int(input())
    print(reverse_digits(x))


# implement ฟังก์ชันนี้ให้ถูกต้อง
def reverse_digits(x):
    num1 = (x%10)*1000
    num2 = (x//10%10)*100
    num3 = (x//100%10)*10
    num4 = x//1000%10

    result = num1+num2+num3+num4
    return result


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_reverse_digits():
    assert reverse_digits(1234) == 4321
    assert reverse_digits(1) == 1000
    print("All OK!")


if __name__ == '__main__':
    main()
