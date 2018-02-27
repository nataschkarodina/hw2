
import numpy as np
import random2

#function that finds the index of a current element
def find_index (matrix, n, m, point):
    for i in range (n):
        for j in range (m):
            if np.any (matrix[i,j] == point):
                current_x = i
                current_y = j
    return (current_x, current_y)

# function that finds the size of the input labirint
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


# читаем лабиринт из файла в матрицу, заменяем все "о" на 0 и все "#" на -1
def read(f, n, m):
    #n = 5
    #m = 6
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
    #print (lab)
    return(lab)

n, m = size(open('lab.txt')) #determine the size of the labirint
print (n, m)
#print the input labirint
lab = read(open('lab.txt'), n, m) #reads the labirint to the matrix
print ('Labirint from input:' )
print (lab )

n = n -1
m = m -1


start_point = lab[0,0]
start_point_x, start_point_y = 0, 0
end_point = lab[n, m]
end_point_x, end_point_y = n, m
current_point = end_point


def wave (x, y, d, n, m, lab):
    lab[x][y] = d
    if y+1<=m:
        if lab[x][y+1] == 0 or (lab[x][y+1] != -1 and lab[x][y+1] > d):
            wave(x,y+1,d+1,n,m,lab)
            #print (x, y+1)
    if x+1 <= n:
        if lab[x+1][y] == 0 or (lab[x+1][y] != -1 and lab[x+1][y] > d):
            wave(x+1,y,d+1,n,m,lab)
    if x-1 >= 0:
        if lab[x-1][y] == 0 or (lab[x-1][y] != -1 and lab[x-1][y] > d):
            wave(x-1,y,d+1,n,m,lab)
    if y-1 >= 0:
        if lab[x][y-1] == 0 or (lab[x][y-1] != -1 and lab[x][y-1] > d):
            wave(x,y-1,d+1,n,m,lab)
    return lab
    main()

lab = wave (start_point_x,start_point_y,1,n,m,lab)
if lab[end_point_x][end_point_y] > 0:
    print('The way can be found')
else:
    print('The way can not be found')
print (lab)

#теперь надо восстановить обратно ход событий
#x = end_point_x
#y = end_point_y







