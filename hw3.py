
import math #подключаем возможность использовать математические функции
x1=float(input('enter x1 '))
x2=float(input('enter x2 '))
if 0 < x1 <1 and 0 < x2 < 1:
    #print ('введенные значения удовлетворяют условию задачи')
    a=math.log1p(x1)
    c=math.pi
    b=math.sin(2*c*x2)
    f=(-2*a)**0.5-b
    print('for x1=', x1, 'and x2=', x2, 'f=', f)
else:
    print ('введенные данные не удовлетворяют условию задачи')


