#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab06_2
# 229223 Sec 002

def classify(list_x) :

    list_a = list(filter(lambda x: isinstance(x, int), list_x))
    list_b = list(filter(lambda x: isinstance(x, float), list_x))  
    list_c = list(filter(lambda x: isinstance(x, str), list_x))

    return list_a, list_b, list_c
    
def main():
    print(classify([10, 'hello', 23.5, 4] ))

if __name__ == '__main__':
    main()
