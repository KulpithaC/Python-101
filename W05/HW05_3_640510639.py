#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW05_2
# 229223 Sec 002

def main():
    assert to_roman_numeral(267) == "CCLXVII"
    assert to_roman_numeral(4) == "IV"
    assert to_roman_numeral(4999) == "MMMMCMXCIX"
    assert to_roman_numeral(40)

def to_roman_numeral(n):
    thousands = 'M' * (n // 1000)
    hundreds = 'CM' if n % 1000 // 100 == 9 else 'D' * (n % 1000 // 500) + 'C' * ((n % 500) // 100)
    tens = 'XC' if n % 100 // 10 == 9 else 'L' * (n % 100 // 50) + 'X' * ((n % 50) // 10)
    ones = 'IX' if n % 10 == 9 else 'V' * (n % 10 // 5) + 'I' * (n % 5)

    result = thousands + hundreds + tens + ones
    result = result.replace('IIII', 'IV')
    result = result.replace('XXXX', 'XL')
    result = result.replace('CCCC', 'CD')
    # print(result)
    return result

if __name__ == '__main__':
    main()