#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW05_2
# 229223 Sec 002
import string

def main():
    assert transform_name('elisabeth andre')
    assert transform_name('lala Divesdentinala')
    assert transform_name('   lena Eive   ')
    assert transform_name('Toyoakini shidai')
    assert transform_name('Yoshimasa Ohmotoyoshi')
    assert transform_name('Tse Michelangelo')

def transform_name(name):
    name = name.strip()
    result = ''
    pos = name.find(' ')
    lenname = len(name[pos+1:])
    lensurname = len(name[:pos])
    if(lenname < 9):
        count = 14 - lenname
        result += name[pos+1:] + '.'
        if(lensurname < count):
            result += name[:lensurname]
        else:
            result += name[:count]
    else:
        count = 14 - lensurname
        if(lensurname <= 5):
            result += name[pos+1:pos+1+count] + '.'
            result += name[:lensurname]
        else:
            result += name[pos+1:pos+10] + '.'
            result += name[:5]

    pos = result.find(".")
    result = result[:0] + result[0].upper() + result[0 + 1:]
    result = result[:pos+1] + result[pos+1].upper() + result[pos + 2:]
   
    return result



if __name__ == '__main__':
    main()
