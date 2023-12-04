#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW03_3
# 229223 Sec 002

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
    if l1 > l2+w2 :
        return False
    elif l2 > l1+w1 :
        return False
    elif t1 > t2+h2 :
        return False
    elif t2 > t1+h1 :
        return False
    else :
        return True
    
def main():
    l1, t1, w1, h1, l2, t2, w2, h2 = int(input())
    print(is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2))


if __name__ == '__main__':
    main()
