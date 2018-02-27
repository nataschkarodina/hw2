
import numpy as np
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO

import matplotlib.pyplot as plt

#input from fasta file
handle = open("fasta_seq.fasta")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
#print (records[3].seq)

# adding blosum62 matrix_____________________________________________________________________________________
#mat = MatrixInfo.blosum62
#testing mat
#print('gw1', mat[seq1[1], seq2[2]])
#w =int(mat[seq1[1], seq2[2]])
#print ('gw2=', w)
#print(mat)
#for i in range(1,n+1):
#    for j in range(1,m+1):
#        print ('i=', i, 'j=', j,'seq1', seq1[j-1], 'seq2', seq2[j-1], 'blos=', (mat[seq1[j-1], seq2[i-1]]))

score = 0 #score
g=10 #penalty for insertion/deletion
w=1 #penalty for mismatch

score_matr = np.zeros((5,5)) #creating a matrix for the score

#filling the  matrix, Wmin
for l in range (5):
    seq1 = records[l-1].seq
    for k in range (5):
        seq2 = records[k-1].seq
        m, n = len(seq1), len(seq2)
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
                        #blos = mat[seq1[j-1], seq2[1]]
                        #print ('blos=', blos)
                        subst += w #int(-mat[seq1[j-1], seq2[i-1]])
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
        #allingning
        seq1_ind=0 #sequence index
        seq2_ind=0
        allign_seq1='' #for saving alligned sequence
        allign_seq2=''

        #restoring the allignment from the matrix
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
        print('for seq1=',l, 'and seq2=', k)
        print (allign_seq1 + '\n' + allign_seq2)
        print('score=', score)
        score_matr[l,k] = score #filling the score matrix


print ('score matrix')
print (score_matr)

#plotting a heatmap
#a = np.random.random((16, 16))
plt.imshow(score_matr, cmap='hot', interpolation='nearest')
#plt.clf()
plt.title('Score representing heatmap')
plt.ylabel('y')
plt.xlabel('x')
plt.show()


