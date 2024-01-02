#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW07_3
# 229223 Sec 002

def main():
    print(num_to_word(1234567))
    print(num_to_word(248))
    print(num_to_word(111))
    print(num_to_word(0))
    print(num_to_word(42641323862))


def num_to_word(num):
    if(num == 0):
        return 'zero'
    elif(0 < num <= 999):
        result = three_digits_to_word(num)
    elif(10**3 <= num < 10**6):
        a, b = divmod(num,10**3)
        if b == 0 :
            result = three_digits_to_word(a) + " thousand "
        elif b != 0 :
            result = three_digits_to_word(a) + " thousand " + three_digits_to_word(b)
    elif(10**6 <= num < 10**9):
        a, b = divmod(num,10**6)
        c, d = divmod(b,10**3)
        if b == 0 :
            result = three_digits_to_word(a) + " million "
        elif b != 0 :
            result = three_digits_to_word(a) + " million " + three_digits_to_word(c) + " thousand " + three_digits_to_word(d)
    elif(10**9 <= num < 10**12):
        a, b = divmod(num,10**9)
        c, d = divmod(b,10**6)
        e, f = divmod(d,10**3)
        if b == 0 :
            result = three_digits_to_word(a) + " billion "
        elif b != 0 :
            result = three_digits_to_word(a) + " billion " + three_digits_to_word(c) + " million " + three_digits_to_word(e) + " thousand " + three_digits_to_word(f)
    return result

def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five",
                 "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]

    ten_list = ["", "", "twenty", "thirty", "forty", "fifty",
                 "sixty", "seventy", "eighty", "ninety"]
    result = []
    a, b = divmod(n,10)
    c, d = divmod(n,100)
    if(n <= 19):
        result = unit_list[n]
    elif(19 < n < 100):
        if b == 0 :
            result = ten_list[a]
        else :
            result = ten_list[a] + "-" + unit_list[b]
    elif(100 <= n <= 999):
        if d == 0 :
            result = unit_list[c] + " hundred"
        else:
            if(d <= 19):
                result = unit_list[c] + " hundred " + unit_list[d]
            elif(19 < d < 100 and d%10 == 0):
                d = d // 10
                result = unit_list[c] + " hundred " + ten_list[d]
            elif(19 < d < 100 and d%10 != 0):
                e = d % 10
                d = d // 10
                result = unit_list[c] + " hundred " + ten_list[d] + "-" + unit_list[e]
    return result


if __name__ == '__main__':
    main()