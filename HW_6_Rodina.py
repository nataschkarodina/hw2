import re

#date
data = '38/11/2017 19.1/7 12-12-8888 72.3.1005 9.31.2018 105.105.105 28.01.2017 05.5.2012'
date = re.findall('(?:[0-2]\d[.][01]?\d[.]\d{1,4})|(?:3[01][.][01]?\d[.]\d{1,4})|(?:[0-2]\d[-][01]?\d[-]\d{1,4})|(?:3[01][-][01]?\d[-]\d{1,4})|(?:[0-2]\d[/][01]?\d[/]\d{1,4})|(?:3[01][/][01]?\d[/]\d{1,4})', data)
print('found dates:', date)

#email
data_line = 'user-name@yandex.com useRR-name@yandex.commmmmmmmmmmmmmm ' \
            'ttt.../ttt nrodina@incras.ru blablablaaa natalia240994.rod@wert.gbgret6768.lkjf@gmail.com n.rodina@incras.com.com'
#milo = re.findall('(?:(?:\s|^)(\w+[-_.]?\w+@{1}\w+\.(?:[a-zA-Z].?){2,6})(?:\W|$))', data_line) #best
#milo = re.findall('(?:(?:\s|^)(\w+[-_.]?\w+@{1}\w+\.(?:[a-zA-Z](\.)?[a-zA-Z]){2,6})(?:\W|$))', data_line) # любимая версия
#milo = re.findall('(?:(?:(?:\s|^)(\w+[-_.]?\w+@{1}\w+\.(?:[a-zA-Z]){2,6})\.(?:[a-zA-Z]){2,6})(?:\W|$))|'
#                     '(?:(?:\s|^)(\w+[-_.]?\w+@{1}\w+\.(?:[a-zA-Z]){2,6})(?:\W|$))', data_line) # любимая версия

#milo = re.findall('(?:(?:\s|^)\w+[-_.]?\w+@\w+[-_.]?\w+\.[a-z]{2,6}(?:\W|$))', data_line) #best
milo = re.findall('(?:(?:\s|^)\w+[-_.]?\w+@\w+[-_.]?\w+\.[a-z]{2,6}(?:\s|$))', data_line) #Julia
print('found emails:', milo)


#text
text_line = 'abrakadabka,storty.  .totellinteresting?one--amazing  merry:chrismas,happy — new year. THE END'
#text = re.findall('([\\s][\\s]+)|([.,-:;?!][.,-:;?!]+)|([.,-:;?!]\\S)', text_line)
text = re.findall('[\s]{2,}|[.,-:;]{2,}|[.,-:;?!]\S', text_line)
print('found errors:', text)


#MAC adress
mac_adress = '66:2A:A1:BB:A8:D3 250:1w:b6:abc:01:g1 09:qw:e1:rt:99:y1 11:aa:bb:cc:d7:a5 1:aa:bb:cc:d7:a5 0F:aa:bb:cc:d7:b5'
#mac2 = re.findall('[A-Fa-f0-9][A-Fa-f0-9]:[A-Fa-f0-9][A-Fa-f0-9]:[A-Fa-f0-9][A-Fa-f0-9]:[A-Fa-f0-9][A-Fa-f0-9]:'
#                  '[A-Fa-f0-9][A-Fa-f0-9]:[A-Fa-f0-9][A-Fa-f0-9]', mac_adress) #  на случай если ток 2 символа
mac2_new = re.findall('((?:[A-Fa-f0-9]{2}:){5}[A-Fa-f0-9]{2})', mac_adress) #  на случай если ток 2 символа
mac16 = re.findall('[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+', mac_adress) #16ричная система
#mac16 = re.findall('[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+:[A-Fa-f0-9]+', mac_adress) #16ричная система
#print('found mac address in case 1:', mac2)
print('found mac address in case 1 new:', mac2_new)
#print('found mac address in case 2:', mac16)

#king-tsar
names = 'peter Peter I Karl karl I  Karl I Ludovig XXI just Karl'
my_regex = re.compile('[A-Z][a-z]+ [IVXLCDM]+')
name = my_regex.findall(names)
print('found Tsars:', name)


