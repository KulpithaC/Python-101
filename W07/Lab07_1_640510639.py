#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# Lab07_2
# 229223 Sec 001
import string

def main():
    assert corner_frame(4)

def corner_frame(n):
    first_row = ' '.join(map(str, range(1, n + 1)))

    # Create each subsequent row
    rows = '\n'.join(map(lambda x:))

    result = f"{first_row}\n{rows}"
    print(result)
    return result

if __name__ == '__main__':
    main()
