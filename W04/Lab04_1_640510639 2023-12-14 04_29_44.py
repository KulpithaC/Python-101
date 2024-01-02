#!/usr/bin/env python3
# Kulpitha Chaimongkol (Kawpoon)
# 640510639
# Rapeepat Treerattrakul (Peet)
# 640510677
# Lab04_1
# 229223 Sec 002

# Done
def main():
    print(german_num_format('1,234'))
    print(german_num_format('1,020.50'))

def german_num_format(num_str):

    num_str = num_str.replace(',', '$')
    num_str = num_str.replace('.', '#')
    
    num_str = num_str.replace('$', '.')
    num_str = num_str.replace('#', ',')

    return num_str

if __name__ == '__main__' :
    main()


