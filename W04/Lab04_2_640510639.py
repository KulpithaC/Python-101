#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab04_1
# 229223 Sec 002

def main():
    assert zodiac_element(1997) == "Yin Fire Ox"
    assert zodiac_element(2022) == "Yang Water Tiger"

def zodiac_element(year):
    result = ""
    if(year % 2 == 0):
        result = "".join([result, 'Yang '])
    else:
        result = "".join([result, 'Yin '])
    
    element = year % 10

    if(element == 0 or element == 1 ):
        result = "".join([result, 'Metal '])
    elif(element == 2 or element == 3):
        result = "".join([result, 'Water '])
    elif(element == 4 or element == 5):
        result = "".join([result, 'Wood '])
    elif(element == 6 or element == 7):
        result = "".join([result, 'Fire '])
    else:
        result = "".join([result, 'Earth '])

    if(year % 12 == 0):
        result = "".join([result, 'Monkey'])
    elif(year % 12 == 1):
        result = "".join([result, 'Rooster'])
    elif(year % 12 == 2):
        result = "".join([result, 'Dog'])
    elif(year % 12 == 3):
        result = "".join([result, 'Pig'])
    elif(year % 12 == 4):
        result = "".join([result, 'Rat'])
    elif(year % 12 == 5):
        result = "".join([result, 'Ox'])
    elif(year % 12 == 6):
        result = "".join([result, 'Tiger'])
    elif(year % 12 == 7):
        result = "".join([result, 'Rabbit'])
    elif(year % 12 == 8):
        result = "".join([result, 'Dragon'])
    elif(year % 12 == 9):
        result = "".join([result, 'Snake'])
    elif(year % 12 == 10):
        result = "".join([result, 'Horse'])
    else:
        result = "".join([result, 'Goat'])

    return result
        



if __name__ == '__main__':
    main()