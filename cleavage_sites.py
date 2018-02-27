from Bio import SeqIO
import re

#открывает файл со всеми пептидазами
handle = open("peptidase_sites_all.fasta")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

# print('test', records[2].seq)
# length = len(records[1])
# print ('length', length)
# n = len(records)

# находит протеазы, для которых известна ровно одна вариация сайта разрезация
k = 0
short_sequences = [] # Setup an empty list
for records in SeqIO.parse("peptidase_sites_all.fasta", "fasta"):
    #if len(records.id) <= 15 :
    k = 0
    seq = records.seq
    m = len(seq)
    for i in range (m):
        if seq[i] == '-':
            k += 1
    if k < 7:
        # Add this record to our list
        short_sequences.append(records)
print("Found %i short sequences" % len(short_sequences))
SeqIO.write(short_sequences, "pep_short.fasta", "fasta")

#переделывает все сайты разрезания для всех протеаз в формат регулярных выражений
cleavage = []
for records in SeqIO.parse("pep_short.fasta", "fasta"):
    seq = records.seq
    m = len(seq)
    i = 0
    cleavage.append ('>')
    cleavage.append(records.id)
    cleavage.append('\n')

    while i <= m-1:
        if i == 0:
            cleavage.append('[')
        #print ('i', i)
        #print (seq[i])
        if seq[i] == '-':
            if i != 0:
                cleavage.append('[')
            cleavage.append('\w')
            cleavage.append(']')
            i = i+1
        elif seq[i] == '/':
            i = i+1
        elif seq[i] == '|':
            i = i+1
            #cleavage.append('|')
        else:
            #cleavage.append(seq[i])
            if i != 0:
                if seq[i-1] == '-' or seq[i-1] == '|' or seq[i-1] == '/':
                    cleavage.append('[')
            if i+1 != m and (seq[i+1] == '/' or seq[i+1] == '|'):
                i = i+1
                cleavage.append(seq[i-1])
                cleavage.append(']')
            else:
                i = i+1
                if i != m-1:
                    cleavage.append(seq[i-1])
                    #cleavage.append('|')
    if i == m:
        if seq[i-1] != '-':
            cleavage.append(']')
        cleavage.append('\n')
    #print (cleavage)
    #cleav = ''.join(cleavage)
cleav = ''.join(cleavage)
#print ('cleav')
#print (cleav)
#запись в файл
file = open('cleave_sites_regular_short.fasta', "w")
file.write(cleav)
file.close()


#finding cleavage sites
my_string = 'MEFPEHGGRLLGRLRQQRELGFLCDCTVLVGDARFPAHRAVLAACSVYFHLFYRDRPAGSRDTVRLNGDIVTAPAFGRLLDFMYEGRLDLRSLPVEDVLAAASYLHMYDIVKVCKGRLQEKDRSLDPGNPAPGAEPAQPP' \
            'CPWPVWTADLCPAARKAKLPPFGVKAALPPRASGPPPCQVPEESDQALDLSLKSGPRQERVHPPCVLQTPLCSQRQPGAQPLVKDERDSLSEQEESSSSRSPHSPPKPPPVPAAKGLVVGLQPLPLSGEGSRELELGAGR' \
            'LASEDELGPGGPLCICPLCSKLFPSSHVLQLHLSAHFRERDSTRARLSPDGVAPTCPLCGKTFSCTYTLKRHERTHSGEKPYTCVQCGKSFQYSHNLSRHTVVHTREKPHACRWCERRFTQSGDLYRHVRKFHCGLVKSLLV'
#search_seq = '[A][PEL][\w][MGL][A][L][VL][V]'
number = 0 # всего количество разрезаний данной последовательности всеми протеазами из списка
coordinates = [] #лист для записи коррдинат всех возможных сайтов разрезания
cutted_sequence = [] #список для записи нарезанных пептидов
cutted = []
for records in SeqIO.parse("cleave_sites_regular_short.fasta", "fasta"):
    search_seq = records.seq
    #print ('cleavage for search', search_seq)
    search_seq = str(search_seq)
    my_regex = re.finditer(search_seq, my_string)
    print ('parse', my_regex)

    #находим вхождения
    matches = [] #список вхождений
    for match in my_regex:
        #print (match.span())
        matches.append(match.span())
    #записываем на будущее коррдинаты ВСЕХ вхождений для всех использованных протеаз в один лист
    if len (matches) != 0: #если количество вхождений не равно нулю, записываем в общий список коррдинаты
        coordinates. append(matches)
    n = len(matches) #количество найденных сайтов разрезания в текущей последовательности для текущей протеазы
    number = number + n #хотим определить общее количество всех возможных сайтов для всех протеаз для текущей последовательности

    # разрезает для текущей протеазы текущую последовательность по найденным сайтам разрезания
    cleav_coord = []
    for i in range (n):
        #print ('match number', i, ':', matches[i])
        match_site = matches[i]

        first_coord = match_site[0] #коррдината первого вхождения
        #print('first coordinate of match number', i, ':', first_coord)
        fisrt_coors = int(first_coord)
        middle_coordinate = first_coord + 2 #рассчитываем координату, после которой происходит разрезаник
        cleav_coord.append(middle_coordinate)
        #print ('cleavage coordinate for match number', i, ': ', middle_coordinate)

        cutted_sequence.append('cleavage number ')
        num = str(i)
        cutted_sequence.append(num)
        cutted_sequence.append(' for protease')
        cutted_sequence.append(search_seq)
        cutted_sequence.append('\n')

        #разрезаем
        for j in range (0, middle_coordinate+1):
            cutted_sequence.append(my_string[j])
        cutted_sequence.append('\n')
        for p in range (middle_coordinate+1, len(my_string)-1):
            cutted_sequence.append(my_string[p])
        cutted_sequence.append('\n')

    # продвинутая разрезалка
    n_c = len(cleav_coord)
    if n_c > 1:
        #print ('n_c', n_c)
        #print('cleav_coord', cleav_coord)


        i = 0
        start = 0
        end = cleav_coord[i]+1
        while end <= cleav_coord[-2]:
            for j in range (start, end):
                cutted.append(my_string[j])
            cutted.append('\n')
            start = end
            if i != cleav_coord[-1]:
                end = cleav_coord[i+1]
            else:
                end = len(my_string)
            i = i+1
    #print ('peptides', cutted)
    #print ('current number of matches', n)
profile = ''.join(cutted)
print ('profile', profile)
file = open('peptide_profile_test.fasta', "w")
file.write(profile)
file.close()

print ('full number of matches', number)

peptide_profile = ''.join(cutted_sequence)
#print (peptide_profile)
#print ('match coordinates', coordinates)

#cutter

    # match1 = matches[1]
    # print (match1)
    # print(match1[0])


