s=str(input('Введите двухзначные числа через пробел ')) #вводить через пробел только двухзначные числа
i=1
k=0
p=[]
if len(s) <= 1:
    print ('no two-digit number')
    exit()
while i-1 <= len(s)-1:
    p=s[i-1]+s[i]
    i+=3
    if p[0] != p[1] and type (p[0]) != str and type(p[1]) != str:
        print (p)
        k+=1
    p=[]
if k == 0:
    print ('No solutions found')






