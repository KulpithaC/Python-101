#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_3
# 229223 Sec 002

def main():
    assert substitute_once('battle', 'b', 'c') == "cattle"
    assert substitute_once('Bidding', 'i', 'u') == "Budding"
    assert substitute_once("doesn't", "n't", ' not') == "does not"

def substitute_once(text, old, new):
    pos = -1
    for i in range(0, len(text) - len(old) + 1):
        if(text[i:i + len(old)] == old):
            pos = i
            break
   
    if(pos != -1):
        result = text[:pos] + new + text[pos + len(old):]
        return result
    return text

if __name__ == '__main__':
    main()