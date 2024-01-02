#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW04_3
# 229223 Sec 002

def main():
    assert substitute_once('battle', 'b', 'c') == "cattle"

    

def substitute_once(text, old, new):
    pos = text.find(old)
   
    if(pos != -1):
        result = text[:pos] + new + text[pos + len(old):]
        return result
    else:
        return text

if __name__ == '__main__':
    main()