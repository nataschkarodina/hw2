
import numpy as np
seq1 = 'ATGCC'
seq2 = 'ATCC'
#seq2 = 'ATGCATGCAT'
#seq2 = 'TGCATGCATGCA'
n, m = len(seq1), len(seq2)
if n > m:
    seq1, seq2 = seq2, seq1
    n, m = m, n

g=10
w=0.5

current_row = range(n+1) # Keep current and previous row, not entire matrix
for i in range(1, m+1):
    previous_row, current_row = current_row, [i]+[0]*n
    for j in range(1,n+1):
        insertions, deletions, substitutions = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
        if seq1[j-1] != seq2[i-1]:
            substitutions += 1
        current_row[j] = min(insertions, deletions, substitutions)

print(current_row[n])







n=4
m=5
Wmin = np.zeros( (n+1,m+1) )

for i in range(n+1):
    for j in range(m+1):
        a1 = Wmin[i,j-1] + 1
        a2 = Wmin[i-1,j] + 1
        a3 = Wmin[i-1,j-1] #+ comparison(seq1[i],seq2[j])
        # Consider borders!
        Wmin[i,] = min( [a1,a2,a3] )
        # Save the previous node to restore optimal alignment

d_L = Wmin[n,m]


