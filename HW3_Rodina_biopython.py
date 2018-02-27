
#for seqond task
from Bio.SubsMat import MatrixInfo
from Bio.pairwise2 import format_alignment
from Bio import pairwise2
from Bio import SeqIO#позволяет осуществлять ввод и вывод последовательностей в различных форматах

#Открываем последовательность
handle = open("fasta_seq.fasta")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
print (records[3])
#print (records[0].id) #first record
#print (records[-1].id) #last record
print ('len=', len(records[0].seq))

seq1 = records[0]
#print ('1', seq1)
seq2 = records [1]
#print ('2', seq2)

#seq1 = 'ATGCC'
#seq2 = 'ATCC'

matrix = MatrixInfo.blosum62
gap_open = -10
gap_extend = -1

#using pairwise2.align.globalds

b_function = pairwise2.align.globalxx(seq1, seq2)
print(format_alignment(*b_function[0]))
#print (b_function.score)
# top_al = al[0]
# s1, s2, score, o, c = top_al
# #print(s1 +'\n'+ s2)
# for a in al:
#     print(format_alignment(*a))
# print('\n')

