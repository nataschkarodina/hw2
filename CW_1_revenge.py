#Control Work 1 Revenge
#Rodina Natalia

#Данная программа определеяет наиболее протяженную область в геноме, содержащую 100% GC-контент (т.е. A, U отсуствуют)

#проверка работы программы осуществляется на файле dm3_chr3R.fa
#На выход программа даем длину наиболее протяженной части и саму последовательность, определенные двумя различными методами
#Программа проверяет, совпадают ли последовательности, определенные разными методами. Первый метод, использующий регулярные вырежения,
# работает гораздо быстрее. Второй метод использовался для самопроверки

from Bio import SeqIO
import re

for records in SeqIO.parse("dm3_chr3R.fa", "fasta"):
    search_seq = records.seq
search_seq = str(search_seq)

#method 1
print ('FIRST METHOD uses re.findall:')
my_regex = re.findall('(?:([GCgc]{2,}))', search_seq)
    #print (my_regex[36])
    #print(type(my_regex))
n = len(my_regex)
length = 2
for i in range (n):
    if len(my_regex[i]) > length:
        length = len(my_regex[i])
        found = my_regex[i]
print('Longest part = ', length)
print ('longest part: ', found)

#second method
print ('SECOND METHOD:')
l = len(search_seq)
k = 0
i = 0
p = 2
current = []
longest = []
while i <= l-1:
    if search_seq[i] == 'G' or search_seq[i] == 'C' or search_seq[i] == 'g' or search_seq[i] == 'c' :
        current.append(search_seq[i])
        k = k+1
    elif i != 0 and (search_seq[i-1] == 'G' or search_seq[i-1] == 'C' or search_seq[i-1] == 'g' or search_seq[i-1] == 'c'):
        if k > p:
            p = k
            longest = current
        current = []
        k = 0
    i = i+1
print('Longest part = ', p)
longest_part = ''.join(longest)
print ('longest part: ', longest_part)

#проверка того, что оба метода дают одинаковый результат
if p == length and longest_part == found:
        print ('Both methods give the same resuls')

#Вывод программы:
# FIRST METHOD uses re.findall:
# Longest part =  26
# longest part:  gcggcggcggcggcggcggcggcggc
# SECOND METHOD:
# Longest part =  26
# longest part:  gcggcggcggcggcggcggcggcggc
# Both methods give the same resuls







