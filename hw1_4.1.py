
s = str(input('Enter the word ')) #слово вводить маленькими буквами
n=len(s)
i=0
n=n-1
k=0 #показатель того, что не палиндром
while n-1 >= i:
    if s[n-i] == s[i]:
        i+=1
    else:
        k=1
        break
if k==1:
    print ('Not a palindrom')
else:
    print ('palindrom')

