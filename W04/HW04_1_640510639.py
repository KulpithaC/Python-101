#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_1
# 229223 Sec 002

def main():
    assert palindrome_without("Banana", 'b') == True
    assert palindrome_without("Swap of paws", 'f') == True
    assert palindrome_without("T", 't') == False
    print(isPalindrome(""))

def isPalindrome(s):
    return s == s[::-1]

def palindrome_without(text, c):
    palin = text.lower()
    C = c.lower()
    if(C in palin):
        result = palin.replace(C, '')
    
    if(len(result) == 0):
        return False

    return isPalindrome(result)

if __name__ == '__main__':
    main()