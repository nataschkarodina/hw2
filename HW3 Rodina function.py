
#Rodina Natalia

from Bio import SeqIO
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#input from fasta file
handle = open("changedspecies.fasta")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

#creating a dictionary of different penalty values for different nucleotide substitution
blos = {'AG': 50, 'AT': 10, 'AC': 10, 'GT': 10, 'GC': 10,'TC': 10,
        'GA': 50, 'TA':10, 'CA': 10, 'TG': 10, 'CG': 10, 'CT': 10,
        'AA':1, 'GG':1, 'TT':1, 'CC':1}


#fuction for the alignment
def align( seq1, seq2 ):
    m, n = len(seq1), len(seq2)
    score = 0 #score
    g = 100 #penalty for insertion/deletion
    #w=1 #penalty for mismatch
    Wmin = np.zeros( (n+1,m+1) ) #start of the allign fuction
    Wmin[0,:] = [k for k in range(m+1)] #filling upper row to don't include in cycle
    Wmin[:,0] = [k for k in range(n+1)] #filling left column
    matrix = [['' for i in range(m+1)] for j in range(n+1)] # create list for saving aligment
    for i in range(1,n+1):
            for j in range(1,m+1):
                #mat = MatrixInfo.blosum62
                matrix[i][0]='v'*i
                insertion = Wmin[i-1,j] + g
                deletion = Wmin[i,j-1] + g
                subst = Wmin[i-1,j-1]
                if seq1[j-1] != seq2[i-1]:
                    NA = str(seq1[j-1])+str(seq2[i-1]) #create a key for the blos dictionary
                    w = int (blos[NA]) #calculate the value of the penalty for the current mismatch
                    subst += w #penalty for the substitution
                values = [deletion,insertion, subst]
                Wmin[i,j] = min(values)
                index_path = values.index(Wmin[i,j]) #deletion, insertion ot subst?
                if index_path == 0: #deletion
                    matrix[i][j]=matrix[i][j-1]+'h' #h - horisontal move
                    score += g
                elif index_path == 1: #insertion
                    matrix[i][j]=matrix[i-1][j]+'v' # v - vertical move
                    score += g
                elif index_path == 2: #match or mismatch
                    matrix[i][j]=matrix[i-1][j-1]+'d' # d - diagonal move
                    score = subst
    #restoring the allignment from the matrix
    seq1_ind=0 #sequence index
    seq2_ind=0
    allign_seq1='' #for saving alligned sequence
    allign_seq2=''

    for i in matrix[n][m]:
        if i=='h':
            allign_seq1+=seq1[seq1_ind]
            seq1_ind+=1
            allign_seq2+='_'
        elif i=='v':
            allign_seq1+='_'
            allign_seq2+=seq2[seq2_ind]
            seq2_ind+=1
        else:
            allign_seq1+=seq1[seq1_ind]
            seq1_ind+=1
            allign_seq2+=seq2[seq2_ind]
            seq2_ind+=1

    #print('for seq1=',k+1, 'and seq2=', l+1)
    #print (allign_seq1 + '\n' + allign_seq2)
    #print('score=', score)
    return(score)

score_matr = np.zeros((5,5)) #creating a matrix for the score

#Comparing the sequences
for l in range (5):
    seq1 = records[l-1].seq
    for k in range (5):
        seq2 = records[k-1].seq
        score_matr[l,k] = align(seq1,seq2) #using the align funtion
#print ('score matrix:')
#print (score_matr)

#plotting a heatmap
#a = np.random.random((16, 16))
#plt.imshow(score_matr, cmap='hot', interpolation='nearest')
#plt.clf()
#plt.title('Heatmap representing the score values')
#plt.ylabel('sequences from 1 to 5')
#plt.xlabel('sequences from 1 to 5')
#plt.legend()
#plt.show()

# Function for trees binding
def bind_trees_new (V1, V2, h1, h2, h):
    n1 = len(V1) #length
    n2 = len(V2)
    # print ('n1=', n1)
    # print ('n2=', n2)
    # print ('V1', V1)
    # print ('V2', V2)
    V = np.zeros((1+n1+n2, 1+n1+n2)) #creating the new matrix of bound trees
    V [0, 1] = h - h1
    V [1, 0] = h - h1
    V[0, n1+1] = h - h2
    V[n1+1,0] = h - h2

    for i in range (0, n1):
        for j in range (0, n1):
            V[i, j] = V1[i-1, j-1]
    for l in range (n1+1, n1+n2+1):
        for m in range (n1+1, n1+n2+1):
            V [l, m] = V2 [l-n1-1, m-n1-1]
    #print ('bind trees new')
    #print (V)
    return(V)

#function finding the minimum of the score matrix and gives the index of this element
def find_min(D):
    min = score_matr[0][1]
    min_i = 0
    min_j = 1
    for i in range (len(score_matr)):
        for j in range(i, len(score_matr)):
            if i != j:
                if score_matr[i,j] < min:
                    min_i = i
                    min_j = j
                    min = score_matr[i,j]
            # else:
            #     continue

    return(min_i, min_j)

Names = ['Macaca', 'Ailuropoda', 'Ornithorhynchus', 'Choloepus', 'Oryctolagus']
Vertexes = [] #вершины
for i in range (len(score_matr)): #задаем список из нулевой матрицы, нулевой высоты и имени для каждого зверя
    Vertexes += [[np.zeros((1,1)), 0, Names[i]]]
name = []
for i in range (len(Names)):
    name.append(Names[i])

while len(Vertexes) > 1:
    i, j = find_min(score_matr) #uses fucntion to find minimum element
    if i > j:
        V = bind_trees_new(Vertexes[i][0], Vertexes[j][0], Vertexes[i][1], Vertexes[j][1], score_matr[i,j]/2)
    else:
        V = bind_trees_new(Vertexes[j][0], Vertexes[i][0], Vertexes[j][1], Vertexes[i][1], score_matr[i,j] / 2)
    #binding of two species with the minimum distance
    Names[i] = Names[i] + '+' + Names[j]
    name.append(Names[i])
    Vertexes[i] = [V, score_matr[i,j]/2, Names[i]]
    del Names[j]
    del Vertexes[j] #удаляем одного из связанных зверей из списка и заменяем оставшегося на
                    # связанного с матрицей V вместо нулевой матрицы и с ненулевой высотой уже,
                    # равной половине расстояния между зверьми

    for k in range(len(score_matr)): #перестраиваем матрицу
        for l in range (len(score_matr)):
            if l == i and i != k:
                a = (score_matr[k, i] + score_matr[k, j])/2
                score_matr[k, i] = a
                score_matr[i, k] = a
            # elif k == l:
            #     continue
    score_matr = np.delete(score_matr, j, 0)
    score_matr = np.delete(score_matr, j, 1)

print ('Final matrix:')
print(V) #выводим итоговую матрицу
#print (name)
#выводим граф
Graph = nx.from_numpy_matrix(np.array(V))
pos=nx.spring_layout(Graph)
nx.draw_networkx_nodes(Graph,pos,
                       nodelist=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                       node_color='b',
                       node_size=300,
                   alpha=1 )

nx.draw_networkx_edges(Graph,pos,width=1.0,alpha=0.5)
labels = {}
for i in range (len(name)):
    labels[i] = name[i]
nx.draw_networkx_labels(Graph,pos,labels,font_size=8)
#G_Graph = nx.draw(Graph, pos, with_labels=True)

plt.show(Graph)

