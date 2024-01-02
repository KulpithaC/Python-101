#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# HW05_1
# 229223 Sec 002
import string

def main():
    assert is_valid_license("9AB8954") == True
    assert is_valid_license("7CD7") == True
    assert is_valid_license("99D12345") == False

def is_valid_license(license_str):
    if(1 < len(license_str) <= 7):
        if(license_str[0].isdigit() and license_str[1].isupper() and license_str[2].isupper() and license_str[3:].isdigit()):
            return True
        elif(license_str[0].isupper() and license_str[1].isupper() and license_str[2:].isdigit() and len(license_str[2:]) < 5):
            return True
        else:
            return False
    else:
        return False
    

if __name__ == '__main__':
    main()