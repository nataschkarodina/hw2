k,l =input ('Enter the field coordinated where the knight is located ') #вводить без пробела
m,n = input ('Enter the field coordinates what we are interested in ')

k=int(k)
l=int(l)
m=int(m)
n=int(n)

#проверка того, что фигура стоит на доске
if 1 <= k <= 8 and 1 <= l <= 8 and 1 <= m <= 8 and 1 <= n <= 8:
    print ('Field coordinates are ok')
else:
    print ('It is not a chess board')
    exit()

#проверка находится ли поле под угрозой
if k+2 == m and l+1 == n:
    print ('Watch out') #watch out = поле под угрозой
elif k-2 == m and l+1 == n:
    print ('Watch out')
elif k+2 == m and l-1 == n:
    print ('Watch out')
elif k-2 == m and l-1 == n:
    print ('Watch out')
else:
    print ('You are save')


