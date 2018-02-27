
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def bind_trees (V1, V2, h1, h2, h):
    n1 = len(V1)
    n2 = len(V2)
    print ('n1=', n1)
    print ('n2=', n2)
    print ('V1')
    print (V1)
    print ('V2')
    print (V2)
    new_row = np.zeros((1,n1+n2+1))
    new_row[0, 1] =  h - h1
    new_row[0, n2+1] = h - h2
    new_colomn = np.zeros((1,n1+n2)).T
    new_colomn[0, 0] = h - h1
    new_colomn[n2, 0] = h - h2
    if np.all(V2 == 0):
        V1_V2 = np.bmat([[V2, np.zeros((n2, n1))], [np.zeros((n1, n2)), V1]])
    else:
        V1_V2 = np.bmat([[V1, np.zeros((n1, n2))], [np.zeros((n2, n1)), V2]])
    V_colomn= np.bmat([[new_colomn, V1_V2]])
    V = np.bmat([[new_row], [V_colomn]])
    print ('V')
    print (V)
    return(V)


def bind_trees_new (V1, V2, h1, h2, h):
    n1 = len(V1) #length
    n2 = len(V2)
    #print ('n1=', n1)
    #print ('n2=', n2)
    #print ('V1', V1)
    #print ('V2', V2)
    V = np.zeros((1+n1+n2, 1+n1+n2)) #creating the new matrix of bound trees
    V [0, 1] = h - h1
    V [1, 0] = h - h1
    #V[0, n1+1] = h - h2
    if np.all(V1 == 0):
        V[n1+1,0] = h - h2
        V[0, n1+1] = h - h2
    else:
        V[n1+1,0] = h - h2
        V[0, n1+1] = h - h2
    #V[n1,0] = h - h2

    for i in range (1, n1):
        for j in range (1, n1):
            V[i, j] = V1[i-1, j-1]
    for l in range (n1+1, n1+n2+1):
        for m in range (n1+1, n1+n2+1):
            V [l, m] = V2 [l-n1-1, m-n1-1]
    #print ('bind trees new')
    #print (V)
    return(V)

def find_min(D):
    #print ('D')
    #print (D)
    min = D[0][1]
    min_i = 0
    min_j = 1
    for i in range (len(D)):
        for j in range(1, len(D)):
            if i == j:
                continue
            else:
                if D[i][j] < min:
                    min_i = i
                    min_j = j
                    min = D[i][j]
    return(min_i, min_j)

D = np.array([[0.0, 790.0, 2811.0, 721.0, 672.0], [790.0, 0.0, 2714.0, 495.0, 220.0], [2811.0, 2714.0, 0.0, 2701.0, 2702.0], [721.0, 495.0, 2701.0, 0.0, 382.0], [672.0, 220.0, 2702.0, 382.0, 0.0]]) #матрица из задания 5.1.
Names = ['Echinops', 'Macaca', 'Sus', 'Ochotona', 'Pongo']
Vertexes = []
for i in range (len(D)):
    Vertexes += [[np.zeros((1,1)), 0, Names[i]]]

print ('Vertexes')
print (Vertexes)

#while len(Vertexes) >= 2:
for f in range (len(Vertexes)-1):
    i, j = find_min(D)
    if i > j:
        V = bind_trees_new (Vertexes[i][0], Vertexes[j][0], Vertexes[i][1], Vertexes[j][1], D[i][j]/2)
    else:
        V = bind_trees_new (Vertexes[j][0], Vertexes[i][0], Vertexes[j][1], Vertexes[i][1], D[i][j] / 2)
    Names[i] = Names[i] + '+' + Names[j]
    Vertexes[i] = [V, D[i][j]/2, Names[i]]
    del Names[j]
    del Vertexes[j]

    for k in range(len(D)):
        for l in range (len(D)):
            if k == l:
                continue
            elif l == i and i != k:
                a = (D[k][i]+D[k][j])/2
                D[k][i] = a
                D[i][k] = a
    D = np.delete(D, j, 0)
    D = np.delete(D, j, 1)

    f = f+1


print(V)

G = nx.from_numpy_matrix(np.array(V))
GG = nx.draw(G, with_labels=True)

plt.show(GG)
