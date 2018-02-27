import numpy as np

#for seqond task

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio.pairwise2 import format_alignment

print('First seq:')
seq1=input()
print('Seqond seq:')
seq2=input()
seq1 = 'ATGCC'
seq2 = 'ATCC'
#seq1 = 'ATGCCATT'
#seq2 = 'ATGCCT'
m, n = len(seq1), len(seq2)

#vreating Wmin and matrix
Wmin = np.zeros( (n+1,m+1) )
Wmin[0,:] = [k for k in range(m+1)] #filling upper row to don't include in cycle
Wmin[:,0] = [k for k in range(n+1)] #filling left column
matrix = [['' for i in range(m+1)] for j in range(n+1)] # create list for saving aligment


#filling the  matrix, Wmin
for i in range(1,n+1):
    for j in range(1,m+1):
        matrix[i][0]='v'*i
        insertion = Wmin[i-1,j]+1
        deletion = Wmin[i,j-1]+1
        subst = Wmin[i-1,j-1]
        if seq1[j-1] != seq2[i-1]:
            subst += 1
        values = [deletion,insertion, subst]
        Wmin[i,j] = min(values)
        index_path = values.index(Wmin[i,j]) #deletion, insertion ot subst?
        if index_path == 0: #deletion
            matrix[i][j]=matrix[i][j-1]+'h' #h - horisontal move
        elif index_path == 1: #insertion
            matrix[i][j]=matrix[i-1][j]+'v' # v - vertical move
        elif index_path == 2: #match or mismatch
            matrix[i][j]=matrix[i-1][j-1]+'d' # d - diagonal move


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


print(allign_seq1 + '\n' + allign_seq2)

print('\n' + 'Biopython aligment')
#_____________________________________________________
#Task 2, lev via biopython

#using pairwise2.align.globalxx
b_function = pairwise2.align.globalxx(seq1, seq2)
print(format_alignment(*b_function[0]))





# matrix = MatrixInfo.blosum62
# gap_open = -1
# gap_extend = -1
#
#
# #using pairwise2.align.globalds
# allign = pairwise2.align.globalds(seq1, seq2, matrix, gap_open, gap_extend)
# #print(format_alignment(zhi))
# top_al = al[0]
# s1, s2, score, o, c = top_al
# #print(s1 +'\n'+ s2)
# for a in al:
#     print(format_alignment(*a))
# print('\n')
#
# #seq1 = 'ATGCATGCATGC'
# #seq2 = 'TTGCATGCATGC'
# #seq2 = 'ATGCATGCAT'
# #seq2 = 'TGCATGCATGCA'


