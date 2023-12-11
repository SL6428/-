import math
a = float(input('Введите число а'))
b = float(input('Введите число b'))
c = float(input('Введите число c'))
D = b**2 - 4*a*c
if D == 0:
    x = -b / (2*a)
    print (x)
elif D < 0:
    print ('Корней нет')
elif D > 0:
    x1 =  (-b + math.sqrt(D))/2*a
    x2 =  (-b - math.sqrt(D))/2*a
    print(x1,x2)
