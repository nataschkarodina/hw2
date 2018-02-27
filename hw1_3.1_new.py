k=input('Enter the number of elements in the list ') #количество желаемых элементов в списках (считаем списки одной длины)
k=int(k)
list1=[]
list2=[]

print ('Enter ', k, 'values for list1')
for i in range(k):
    x=input()
    x=int(x)
    list1.insert(i,x)

print ('Enter ', k, 'values for list1')
for i in range(k):
    x=input()
    x=int(x)
    list2.insert(i,x)

listSum=[]
for i in range(k):
    listSum.insert(i,0)
#print (listSum)

for i in range(k):
    listSum[i]=list1[i]+list2[i]

print ('Sum list is= ', listSum)
