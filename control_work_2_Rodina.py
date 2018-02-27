
import numpy as np
import matplotlib.pyplot as plt
import random2

#function that finds the index of the current_point in the matrix
def find_index (matrix, n, m, point):
    for i in range (n):
        for j in range (m):
            if np.any (matrix[i,j] == point):
                index = i, j
    return (index)

#generate a special matrix n*m
n = 10
m = 10
#fill the matrix with values from 0 to n*m to use it in the creation of the labirint
t = 0
lab = np.zeros((n, m))
for i in range (n):
    for j in range (m):
        lab[i,j] = t
        t = t+1

list_of_visited = []
start_point = lab[0,0]
stop_point = lab[9,9]
current_point = start_point
indexes = find_index(lab, n, m, current_point)
#print ('indexes', lab[indexes])
# print (indexes[0])
not_visited_list = []
for i in range (n):
    for j in range (m):
        not_visited_list.append(lab[i,j])
#while stop_point not in list_of_visited:
while len(not_visited_list) != 0:
    not_visited = []
    if current_point not in list_of_visited:
        current_list = []
        print ('list of visited before', list_of_visited)
        print ('current_point in the beggining', current_point)
        list_of_visited.append(current_point)
        print ('list of visited', list_of_visited)
        itemindex = find_index (lab, n, m, current_point)
        print ('intem_index of current point', itemindex)
        i = itemindex[0]
        j = itemindex[1]
        print ('i,j', i,j)
        if j+1 <= 9:
            if lab[i, j+1] not in list_of_visited:    #1
                current_list.append(lab[i, j+1])
                not_visited.append(lab[i, j+1])
        if i+1 <= 9:
            if lab[i+1, j] not in list_of_visited:     #2
                current_list.append(lab[i+1, j])
                not_visited.append(lab[i+1, j])
        if i-1 >= 0:
            if lab[i-1, j] not in list_of_visited:    #3
                current_list.append(lab[i-1, j])
                not_visited.append(lab[i-1, j])
        if j-1 >= 0:
            if lab[i, j-1] not in list_of_visited:    #4
                current_list.append(lab[i, j-1])
                not_visited.append(lab[i, j-1])
        if len(current_list) !=0:
            next_step = random2.choice(current_list) #случайный элемент непустой последовательности.
        itemindex = find_index (lab, n, m, next_step)
        print ('item_index of next step', itemindex)
        print ('next_step', next_step)
        print ('list_of_visited', list_of_visited)
        print ('current_list', current_list)
        current_point = next_step
        print ('going to next step')
    else:
        if len(not_visited) !=0:
            next_step = random2.choice(not_visited)

print ('lab', lab)
print ('final print of visited', list_of_visited)

#from website
#rdl = list(map(int,input().split()))
#n, m = rdl
#for i in range(n):
#        rdl = input()
#        cur = []
#        for k in range(m):
#            if int(rdl[k]) == 1:
#                cur.append(-1)
#            else:
#                cur.append(int(rdl[k]))
#        lab.append(cur)
#print ('lab', lab)

