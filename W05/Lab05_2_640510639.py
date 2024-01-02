#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab05_2
# 229223 Sec 002

def main():
    assert compare_date('28/2/2023', '1/1/2024') == -1
    assert compare_date('29/2/2024', '1/1/2024') == 1

def compare_date(d1, d2):
    pos = d1.index('/')
    day1 = int(d1[:pos])
    pos2 = d1.find('/', pos+1)
    month1 = int(d1[pos+1:pos2])
    year1 = int(d1[pos2+1:])
    pos = d2.index('/')
    day2 = int(d2[:pos])
    pos2 = d2.find('/', pos+1)
    month2 = int(d2[pos+1:pos2])
    year2 = int(d2[pos2+1:])

    if year1 < year2:
        return -1
    elif year1 > year2:
        return 1

    if month1 < month2:
        return -1
    elif month1 > month2:
        return 1

    if day1 < day2:
        return -1
    elif day1 > day2:
        return 1
    
    return 0


if __name__ == '__main__':
    main()