#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_1
# 229223 Sec 002

def main():
    assert palindrome_without("Banana", 'b') == True
    assert palindrome_without("Swap of paws", 'f') == True
    assert palindrome_without("T", 's') == True
    print(isPalindrome("A"))
    print(palindrome_without("", "a"))

def isPalindrome(s):
    return s == s[::-1]

def palindrome_without(text, c):
    if(len(text) == 0):
      return False
    palin = text.lower()
    C = c.lower()
    result = palin.replace(C, '')

    if(len(result) == 0 or result == ""):
        return False
    
      

    return isPalindrome(result)

if __name__ == '__main__':
    main()