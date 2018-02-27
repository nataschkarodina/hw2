#lesson 3 - 24.02.2018
#Objects an classes

#создаем класс
class Kmer:
    counter = 0
    sequence = ''
    #pass #ничего не делает, но нужно, чтобы класс не был пустым

    def __init__(self, kmer_name):
        self.sequence = kmer_name

    def increase(self):
        self.counter +=1

    def increase_n(self, n):
        self.counter += n

x = Kmer('ATG')
print('x', x)

x.variable = 10
print('value', x.variable)
print ('counter', x.counter)

y = Kmer('CCC')
print(y.counter)
y.increase()
y.increase()
print (y.counter)

y.increase_n(5)
print(y.counter)
print(y.sequence)

seq = 'ATGATTGCCATGG'
seq_lng = len(seq)
kmer_size = 3
#создаем словарь, в котором последовательность к-мера является ключом
kmer_dict = {}
for index in range (seq_lng - kmer_size + 1):
    current_kmer = seq[index:(index+kmer_size)]
    print (current_kmer)
    #если такой ключ в словаре уже есть, значит такой к-мер нам уже встречался. как это проверить?
    if current_kmer in kmer_dict:
        kmer_dict[current_kmer].increase()
    else:
        kmer_dict[current_kmer] = Kmer(current_kmer)
