import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO

with open ('species.fasta') as file:
    with open ('changedspecies.fasta', 'w') as ouf:
        for record in SeqIO.parse(file, "fasta"):
            rec = record.id
            seq = record.seq
            ouf.write('>')
            ouf.write(rec)
            ouf.write('\n')
            for i in range (len(seq)):
                if seq[i] == '-':
                    continue
                else:
                    ouf.write(str(seq[i]))
            ouf.write('\n')

