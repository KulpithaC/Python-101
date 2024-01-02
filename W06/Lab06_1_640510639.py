#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab06_1
# 229223 Sec 002


def main():
    assert triangle(10)
    # assert triangle(7)


def triangle(n):
    top_part = '\n'.join(map(lambda i: '*' + '.' * (2 * i - 3) + '*' if i > 1 else '*', range(1, n)))
    middle_part = '* ' * n + '\n'
    result = f"{top_part}\n{middle_part}"
    return result


def test_triangle():

    T3 = '''*
*.*
* * *
'''

    T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")


if __name__ == '__main__':
    main()
