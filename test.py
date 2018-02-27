
import numpy as np


f = open('lab.txt')

def size (f):
    #f = open('lab.txt')
    k = 0
    s =0
    row = []
    for line in f:
        k = k +1 #определяем количество сторок по их количеству
        for l in line.split():
            row.append(l)
    m = len(row[1]) #определяем количество столбцов по длине строки

    print('n, m', k, m)
    return (k, m)

rows, colums = size(f)
print (rows, colums)

#########
#read labirint from file and chande "o" to 0 and "#" to -1
f = open('lab.txt')
n = rows
m = colums
lab = np.zeros((n, m))
a = 0
b = 0
for i in f.readlines():
    b = 0
    for l in i.strip():
        #print (a, b)
        #print (str(l))
        if l == '\n':
            a += 1
            b =0
        if str(l) == "o":
            lab[a,b] = 0
        elif str(l) == "#":
            lab [a,b] = -1
        b += 1
    a += 1
print ('labirint', lab)



