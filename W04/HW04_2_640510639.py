#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_2
# 229223 Sec 002

def main():
    assert rotate(12345, 3) == 34512
    assert rotate(12345, 2) == 45123
    assert rotate(12345, -3) == 45123
    assert rotate(12345, -103) == 45123

def rotate(num, pos):
    digit = len(str(num))
    if(pos > 0):
        pos = pos % digit
        change = num % 10**pos
        result = change * 10**(digit - pos) + (num // 10**pos)
    else:
        pos = abs(pos)
        pos = pos % digit
        change = num % 10**(digit-pos)
        result = (change * 10**pos) + (num // 10**(digit - pos))

    return result


if __name__ == '__main__':
    main()