#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# Lab07_2
# 229223 Sec 002
import string

def main():
    assert uniform("HaPpY")


def uniform(line):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    lowercount = len(list(filter(lambda x: x.islower(), line)))
    uppercount = len(list(filter(lambda x: x.isupper(), line)))
    if lowercount > uppercount:
        result = line.lower()
    elif lowercount < uppercount:
        result = line.upper()
    else:
        if line[0] in lower:
            result = line.lower()
        elif line[0] in upper:
            result = line.upper()
    return result 

if __name__ == '__main__':
    main()