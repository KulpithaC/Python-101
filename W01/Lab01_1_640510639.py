import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
s = (a+b+c)/2
area = int(math.ceil(math.sqrt(s*(s-a)*(s-b)*(s-c))))

print('area:', area)
