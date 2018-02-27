
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio.pairwise2 import format_alignment

print('First seq:')
seq1=input()
print('Seqond seq:')
seq2=input()



#using pairwise2.align.globalxx
yest = pairwise2.align.globalxx(seq1, seq2)
print(format_alignment(*yest[0]))




 matrix = MatrixInfo.blosum62
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


