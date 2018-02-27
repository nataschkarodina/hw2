
n=int(input('enter the wanted number of calculations '))
#n=int(n)
f0=0
f1=1
if n <= 1:
    print ('i= 1 f=', f0)
else:
    print ('i= 1 f=', f0)
    print ('i= 2 f=', f1)

if n > 2:
    for i in range (n-2):
        f=f0+f1
        f0=f1
        f1=f
        print('i=',i+3,'f=', f)
else:
    exit()




