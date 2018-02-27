print ('Please, enter the values you want to check')
a = float(input ('a= '))
b = float(input ('b= '))
c = float(input ('c= '))
d = float(input ('d= '))
if a == b and c == d:
    print ('Yes')
elif a == c and b == d:
    print ('Yes')
elif a == d and c == b:
    print ('Yes')
else:
    print ('No')
