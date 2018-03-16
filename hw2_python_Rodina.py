from Bio import SeqIO
import pandas as pd

class Kmer:
    counter = 0 #shows how many times we meet the k-mer in the sequence
    sequence = '' #The k-mer sequence
    loc = [] #locuses
    loc_end = []

    def __init__(self,kmer_name):
        self.sequence = kmer_name
    
    def increase(self):
        self.counter += 1
        
    def increase_n(self, n):
        self.counter += n

    def locuses(self, seq):  # searching for locuses (initial and end coordinated)
        length = len(self.sequence)
        m = len(seq) - length + 1
        for index in range(m):
            current_kmer = seq[index:(index + length)]
            if current_kmer == self.sequence:
                self.loc.append(index)
                self.loc_end.append(index + length)
        #print('locus start', self.loc)
        #print('locus end', self.loc_end)

    def loc_dataframe(self):  # output of the locuses as a dataframe
        output = pd.DataFrame(data={'end': self.loc_end, 'start': self.loc})
        return (output)

#read the sequences from file
handle = open("seq_y_pestis.fasta")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
print (len(records))
kmer_size = 23
seq = ''
kmer_dict = {}
max_kmer = 0
best_seq = []

#go on for every sequence from the file:
for record in records:
    seq = record.seq
    seq_lng = len(seq)

    # create a dictionary of k-mers and their occurrence in the sequence
    for index in range(seq_lng - kmer_size + 1):
        current_kmer = seq[index:(index + kmer_size)]
        #print(current_kmer)
        if current_kmer in kmer_dict:
            kmer_dict[current_kmer].increase()
        else:
            kmer_dict[current_kmer] = Kmer(current_kmer)


# finding the most popular k-mer
max = 0
for kmer in kmer_dict:
    current = kmer_dict[kmer]
    if current.counter > max:
        max = current.counter
        best_seq = kmer
        #best_seq = kmer_dict[kmer]
print ('the occurance of the most frequent k-mer', max) # the occurance
print('the sequence of the most frequent kpmer', best_seq) #the sequence
common_kmer = Kmer(best_seq)
common_kmer.locuses(seq)
#shows all the locuses of all found k-mers as a dataframe
print('The table of the found locuses and their positions for the most frequent k-mer')
print(common_kmer.loc_dataframe())

