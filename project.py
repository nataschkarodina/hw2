
import os
from Bio import SeqIO
import re

#understanding the type of data to work

#print ('Choose the tissue type to get the peptide profile')
#print ('1 - is ....', '\n', '2 - is ....')
# 1 - Adrenal
# 2 - Bladder
# 3 - Breast
# 4 - Central Nervous System
# 5 - Colon
# 6 - Esophagus
# 7 - Female Reproductive System
# 8 - Haematopoietic And Lymphoid Tissue
# 9 - Kidney
# 10 - Liver
# 11 - Lung
# 12 - Pancreas
# 13 - Prostate
# 14 - Salivary Gland
# 15 - Skin
# 17 - Small Intestine
# 18 - Stomach
# 19 - Testes
# 20 - Thyroid
#tissue_type = input () #the input data for the cancer type

#open fast file for breast cancer specific sequences
#if tissue_type == 3:

#open fast file for breast cancer specific sequences
# handle_prot = open("breat_seqs.fasta")
# records_prot = list(SeqIO.parse(handle_prot, "fasta"))
# handle_prot.close()
#
# #open fast file for breast specific peptidases
# handle_pept = open("breast_peptidases.fasta")
# records_pept = list(SeqIO.parse(handle_pept, "fasta"))
# handle_pept.close()
#
# n = len(records_prot) #number of proteins
# m = len (records_pept) #number of peptidases

#cutter
my_string = 'MEFPEHGGRLLGRLRQQRELGFLCDCTVLVGDARFPAHRAVLAACSVYFHLFYRDRPAGSRDTVRLNGDIVTAPAFGRLLDFMYEGRLDLRSLPVEDVLAAASYLHMYDIVKVCKGRLQEKDRSLDPGNPAPGAEPAQPP' \
            'CPWPVWTADLCPAARKAKLPPFGVKAALPPRASGPPPCQVPEESDQALDLSLKSGPRQERVHPPCVLQTPLCSQRQPGAQPLVKDERDSLSEQEESSSSRSPHSPPKPPPVPAAKGLVVGLQPLPLSGEGSRELELGAGR' \
            'LASEDELGPGGPLCICPLCSKLFPSSHVLQLHLSAHFRERDSTRARLSPDGVAPTCPLCGKTFSCTYTLKRHERTHSGEKPYTCVQCGKSFQYSHNLSRHTVVHTREKPHACRWCERRFTQSGDLYRHVRKFHCGLVKSLLV'
#search_seq = '[A][PEL][\w][MGL][A][L][VL][V]'
number = 0 # всего количество разрезаний данной последовательности всеми протеазами из списка
coordinates = [] #лист для записи коррдинат всех возможных сайтов разрезания
cutted_sequence = [] #список для записи нарезанных пептидов
cutted = []
k = 0
for records in SeqIO.parse("cleave_sites_regular_short.fasta", "fasta"):
    search_seq = records.seq
    #print ('cleavage for search', search_seq)
    search_seq = str(search_seq)
    my_regex = re.finditer(search_seq, my_string)
    #print ('parse', my_regex)

    #находим вхождения
    matches = [] #список вхождений
    for match in my_regex:
        #print (match.span())
        matches.append(match.span())
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


    # продвинутая разрезалка
    n_c = len(cleav_coord)
    if n_c > 1:
        #print ('n_c', n_c)
        #print('cleav_coord', cleav_coord)
        i = 0
        start = 0
        end = cleav_coord[i]+1
        while end <= cleav_coord[-2]:
            #print ('number of cleavage', i)
            for j in range (start, end):
                cutted.append(my_string[j])
            cutted.append('\n')
            start = end
            if start != cleav_coord[-1]:
                end = cleav_coord[i+1]
            else:
                end = len(my_string)
                for j in range (start, end):
                    cutted.append(my_string[j])
                k = k+1
            i = i+1
            k = k+1 #calculatind the number of cleavages
    # elif n_c == 1:
    #     k += 1
    #     start = 0
    #     end = cleav_coord[0]
    #     for j in range (start, end):
    #         cutted.append(my_string[j])
    #     cutted.append('\n')
    #print ('peptides', cutted)
    #print ('current number of matches', n)
profile = ''.join(cutted)

print ('number of lines in cutted', k)

print ('profile', profile)
file = open('peptide_profile_short.txt', "w")
file.write(profile)
file.close()

print ('full number of matches', number)

peptide_profile = ''.join(cutted_sequence)
#print (peptide_profile)
#print ('match coordinates', coordinates)

profile = open('peptide_profile_short.txt')
good_peptides = []
pep = 0
for line in profile:
    if len(line)<= 20 and len(line) > 10 :
        good_peptides.append(line)
        pep += 1
MHC_profile = ''.join(good_peptides)
#print ('MHC profile', MHC_profile)
print ('number of good peptides', pep)













