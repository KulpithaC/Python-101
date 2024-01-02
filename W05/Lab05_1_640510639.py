#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab05_1
# 229223 Sec 002

def main():
    assert is_wildcard_match('c??t', 'cart') == True


def is_wildcard_match(pattern, word):
    if(len(pattern) == len(word)):
        pos = pattern.find('?')
        count = pattern.count('?')
        if(pattern[:pos] == word[:pos] and pattern[pos+count:] == word[pos+count:]):
            return True
    return False


if __name__ == '__main__':
    main()