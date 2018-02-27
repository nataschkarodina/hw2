print ('Enter the numbers') #вводить числа без пробела
s=input()
#print(s)
i=1
k=0
if len(s) <= 1:
    print ('Is not a sequence of numbers')
    exit()
while i <= len(s)-1:
    if s[i] >= s[i-1]:
        i=i+1
    else:
        k=1
        break
if k == 1:
    print ('No')
else:
    print ('YEs')

