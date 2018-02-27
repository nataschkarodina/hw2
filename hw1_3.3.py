
import math
e = 2.71828 #константа Эйлера
error = e/100*5 #разрешенная погрешность
S = 1
n=1
while (error <= (S-e)) or ((e-S) >= error):
    z = math.factorial(n)
    S = S+1/z
    n=n+1
    #print('S= ',S)
    #print ('n= ', n)
print ('final S=', S)
print ('final error= ', S-e)
print ('error limitations', error)
print ('final n= ', n)








