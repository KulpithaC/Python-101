#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# HW06_1
# 229223 Sec 002

def main():
                # 012345678, len = 9
    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))
                # 0123456789, len = 10
    print(decode("aceiklmr- ", '''
3 9 5 3 4 2 9 3 1 2 8 1 7 2 0 86 .
'''))
    
    print(decode("", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))

    print(decode("", '''
3 9 5 3 4 2 9 3 1 2 8 1 7 2 0 86 .
'''))
    
    print(decode("abcdefghijklmnopqrstuvwxyz", '''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 .
'''))
    
    print(decode("aaa", '''
0 0 0 .
'''))
    
    print(decode("abc", '''
0 1 2 -1 -2 -3 .
'''))
    
    print(decode("aAa", '''
0 1 -3 .
'''))

def decode_helper(code_table, str_index):
    if str_index == '.' or code_table == '':
        return '\n'
    elif(int(str_index) > 0):
        if(int(str_index) < len(code_table)):
            return code_table[int(str_index)]
        else:
            return '_'
    else:
        if(abs(int(str_index)) <= len(code_table)):
            return code_table[int(str_index)]
        else:
            return '_'

def decode(code_table, text):
    lines = text.split()
    decoded_lines = list(map(lambda s: decode_helper(code_table, s), lines))
   
    result = ''.join(decoded_lines)
    return result

if __name__ == '__main__':
    main()

