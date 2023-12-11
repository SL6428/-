import math
while True:
    try:
        a = int(input('Введите число а'))
        b = int(input('Введите число b'))  
        c = int(input('Введите число c'))
    except ValueError:
        print ('неправильный тип данных')
    else:
        D = (b**2) - (4*a*c)
        if D == 0:
            x = -b / (2*a)
            print (x)
        elif D < 0:
            print ('Корней нет')
            break
        elif D > 0:
            x1 =  (-b + math.sqrt(D))/(2*a)
            x2 =  (-b - math.sqrt(D))/(2*a)
            print(x1,x2)
            break

