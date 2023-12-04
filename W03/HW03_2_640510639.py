#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_2
# 229223 Sec 002

def main():
   hour1, min1, period1 = input().split()
   hour1, min1 = int(hour1), int(min1)
   hour2, min2, period2 = input().split()
   hour2, min2 = int(hour2), int(min2)
   print(min_diff(hour1, min1, period1, hour2, min2, period2))
    
def min_diff(hour1, min1, period1, hour2, min2, period2):
    total_min1 = (hour1 % 12) * 60 + min1 + (0 if period1 == 'AM' else 12 * 60)
    total_min2 = (hour2 % 12) * 60 + min2 + (0 if period2 == 'AM' else 12 * 60)

    result = abs(total_min1 - total_min2)

    return result

if __name__ == '__main__':
    main()