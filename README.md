# Homework 2

This skript finds all k-mers with the length = 23 in a sequence

# Usinfg the skript 

You will need to download the skipt hw2_python_Rodina.py

## Inout file
You can download and you sequence file seq_y_pestis.fasta.
If you use your own sequence file don't forget to change the name of file in the skript

Change the current file name to that of yours. Remember, the file shoud be in fasta format
```
handle = open("seq_y_pestis.fasta")
```
## The k-mer length

The current used k-mer length in the skript is 23. 
You can change the length to the one you want. 
Just change it in the skript:
```
kmer_size = 23
```


## What is the output?

The skript will provide you information about the most frequent k-mer in the sequence.
It will give its sequence, position and how many times it is present in the main sequence.

```
the occurance of the most frequent k-mer 31
the sequence of the most frequent kpmer CTACATGGATGTATTTACGGCGT
The table of the found locuses and their positions for the most frequent k-mer
        end    start
0    114065   114042
1    257534   257511
2    600525   600502
3    637973   637950
4    723894   723871
....
```
If you want to see all the present k-mers in the studied sequence, just remove the hash from the skrip in the section
create a dictionary of k-mers and their occurrence in the sequence:

```
for index in range(seq_lng - kmer_size + 1):
        current_kmer = seq[index:(index + kmer_size)]
        #print(current_kmer)
        if current_kmer in kmer_dict:
            kmer_dict[current_kmer].increase()
        else:
            kmer_dict[current_kmer] = Kmer(current_kmer)
```

* Hope you liked the skript
* And found it useful
* Good luck!
