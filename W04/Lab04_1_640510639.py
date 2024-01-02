#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab04_1
# 229223 Sec 002

def main():
    assert german_num_format("1,234") == "1.234"
    # num_str = input("")
    # print(german_num_format(num_str))


def german_num_format(num_str):
    result = ''
    for i in range(len(num_str)):
        if(num_str[i] == '.'):
            result += ','
        elif(num_str[i] == ','):
            result += '.'
        else:
            result += num_str[i]

    return result

if __name__ == '__main__':
    main()