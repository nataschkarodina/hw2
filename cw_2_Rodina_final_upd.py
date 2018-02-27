import numpy as np
import numpy as np
import sys
import random2


# function that finds the size of the input labirint
def size (f):
    #f = open('maze.txt')
    k = 0
    s =0
    row = []
    for line in f:
        k = k +1 #определяем количество сторок по их количеству
        for l in line.split():
            row.append(l)
    m = len(row[1]) #определяем количество столбцов по длине строки
    #print('n, m', k, m)
    return (k, m)


# читаем лабиринт из файла в матрицу, заменяем все "о" на 0 и все "#" на -1
def read(f, n, m):
    #n = 5
    #m = 6
    maze = np.zeros((n, m))
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
                maze[a,b] = 0
            elif str(l) == "#":
                maze[a,b] = -1
            b += 1
        a += 1
    #print (maze)
    return(maze)

n, m = size(open('lab.txt')) #determine the size of the labirint
#print (n, m)
#print the input labirint
maze = read(open('lab.txt'), n, m) #reads the labirint to the matrix
print ('Labirint from input:' )
print (maze)

n = n -1
m = m -1

start_point = maze[0,0]
start_point_x, start_point_y = 0, 0
end_point = maze[n, m]
end_point_x, end_point_y = n, m

#check that it is a labirint
# flag = 0
# check = n*m
# for i in range (n):
#     for j in range (m):
#         if maze[i,j] == 0:
#             flag += 1
# if flag == check:
#     for i in range (n):
#         for j in range (m):
#             a = start_point_x
#             b = start_point_y
#             l = [] #list for writing the path
#             l.append([str(a), ', ', str(b)])
#             while a != n and b != m:
#                 t = random2.randint(1, 2)
#                 if t == 1 and b+1 <= m:
#                     l.append([str(a), ', ' , str(b+1)])
#                     b = b + 1
#                 elif t == 2 and a+1 <= n:
#                     l.append([str(a+1), ', ', str(b)])
#                     a = a + 1
#     file = open('path.txt', "w")
#     for i in l:
#         file.write(''.join(i) + '\n')
#     file.close()
#     print ('there are no walls - you can choose any way. Written to file path.txt')
#     exit()


#current_point = end_point

# ищет, есть ли выход из лабиринта и присваивает каждой клетке, по которой можно пройти значение уровня воды
def wave (x, y, d, maze):
    sys.setrecursionlimit(1900)
    maze[x][y] = d
#    while maze[end_point_x, end_point_y] == 0:
    if y+1<= m:
        if maze[x][y+1] == 0 or (maze[x][y+1] != -1 and maze[x][y+1] > d):
            wave(x,y+1,d+1, maze)
    elif x+1 <= n:
        if maze[x+1][y] == 0 or (maze[x+1][y] != -1 and maze[x+1][y] > d):
            wave(x+1,y,d+1, maze)
    elif x-1 >= 0:
        if maze[x-1][y] == 0 or (maze[x-1][y] != -1 and maze[x-1][y] > d):
            wave(x-1,y,d+1, maze)
    elif y-1 >= 0:
        if maze[x][y-1] == 0 or (maze[x][y-1] != -1 and maze[x][y-1] > d):
            wave(x,y-1,d+1, maze)
    #print (x,y, d)
    return maze
    #main()

def wave_upd (start_point_x, start_point_y, d, maze):
    sys.setrecursionlimit(1900)
    maze[start_point_x][start_point_y] = d
    print ('n,m', n, m)
#    while maze[end_point_x, end_point_y] == 0:
    for x in range (n+1):
        for y in range (m+1):
            if maze [x,y] != -1 and maze [x,y] != 0:
                if y+1 <= m:
                    if maze[x][y+1] == 0 or (maze[x][y+1] != -1 and maze[x][y+1] > d):
                        maze[x, y+1] = d + 1
                if x+1 <= n:
                    if maze[x+1][y] == 0 or (maze[x+1][y] != -1 and maze[x+1][y] > d):
                        maze[x+1, y] = d + 1
                if x-1 >= 0:
                    if maze[x-1][y] == 0 or (maze[x-1][y] != -1 and maze[x-1][y] > d):
                        maze[x-1, y] = d + 1
                if y-1 >= 0:
                    if maze[x][y-1] == 0 or (maze[x][y-1] != -1 and maze[x][y-1] > d):
                        maze[x, y-1] = d + 1
                #print ('x, y', x, y)
                #print ('d level', d)
                d = d + 1

    #print (x,y, d)
    return maze
    #main()

# восстанавливает путь по уровню воды и записывает этот путь в файл
def find_path(a, b, n, m, maze):
    #a = end_point_x
    #b = end_point_y
    #теперь надо восстановить обратно ход событий
    c= [] #list for writing the path
    c.append([str(a), ', ', str(b)])
    print (n,m)
    while maze[a][b] != 1:
        choose_index_a = []
        choose_value_a = []
        choose_index_b = []
        choose_value_b = []
        if  b-1 >= 0 and maze[a, b-1] < maze [a,b] and maze[a, b-1] != -1 :
            choose_index_b.append(b-1)
            choose_value.append(maze[a, b-1])
        if maze [a-1, b] < maze [a,b] and a-1 >= 0 and maze[a-1 , b] != -1:
            choose_index_a.append(a-1)
            choose_value.append(maze[a-1 , b])
        if b+1 <= m and maze [a, b+1] < maze [a,b] and maze[a, b+1] != -1:
            choose_index_b.append(b+1)
            choose_value.append(maze[a, b+1])
        if a+1 <= n and maze [a+1, b] < maze [a,b] and maze[a+1, b] != -1:
            choose_index_a.append(a+1)
            choose_value.append(maze[a+1, b])

        if len(choose_value) != 0:
            t_a = max(choose_value_a)
        
        #print (t_a)
        print (choose_value_b)
        for i in range (0, len(choose_index_a)):
            if choose_value_a == t_a:
                a = t_a[i]
        for j in range (0, len(choose_index_b)):
            if choose_value_b == t_b:
                b = int(t_b[j])
        c.append([str(a), ', ' , str(b)])



        # if (maze[a][b]-1 == maze[a][b-1]) and b-1 >= 0:
        #     c.append([str(a), ', ' , str(b-1)])
        #     b = b - 1
        # elif (maze[a][b]-1 == maze[a-1][b]) and a-1 >=0:
        #     c.append([str(a-1), ', ', str(b)])
        #     a = a - 1
        # elif maze[a][b]-1 == maze[a][b+1] and b+1 <= m:
        #     c.append([str(a), ', ' , str(b+1)])
        #     b = b + 1
        # elif (maze[a][b]-1 == maze[a+1][b]) and a+1 <= n:
        #     c.append([str(a+1), ', ', str(b)])
        #     a = a + 1

        #print ('I am working')
    #write output to file
    file = open('path.txt', "w")
    for i in c[::-1]:
        file.write(''.join(i) + '\n')
    file.close()
    return (c)

#program itself

maze = wave_upd (start_point_x,start_point_y,1,maze)
if maze[end_point_x][end_point_y] > 0:
    print('The path can be found. You can find it in path.txt')
    a = end_point_x
    b = end_point_y
    find_path(a, b, n, m, maze) # function find_path finds the path and writes it in file
else:
    print('The path can not be found, sorry')
print (maze)

#print(c)



