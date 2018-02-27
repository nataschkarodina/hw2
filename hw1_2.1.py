print ('Enter the triangle lengths')
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
if a == b == c :
    print ('Треугольник равносторонний')
elif a == b or a == c or c == b:
    print ('Треугольник равнобедренный')
else:
    print ('Треугольник разносторонний')


