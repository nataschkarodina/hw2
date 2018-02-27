import re
import requests

#parsing end filtering IDs to get set of new url's for protheases with known cleavage sites
input_file = open("Merops_id.txt", "r")
idid = input_file.read().splitlines()

k = open('new_IDs_new.txt', "w") #file for peptidases cleavage sites
f = open('new_urls.txt', "w") #file with urls for p with known sites for further use
#
for idd in idid:
    url = "https://www.ebi.ac.uk/merops/cgi-bin/pepsum?id=" + idd #generate url
    data = requests.get(url).text #parse web page
    s = [] #site output
    #finding cleavage sites
    res = re.findall('[\w,-]+/[\w,-]+/[\w,-]+/[\w,-]+<a onMouseover="" onMouseout=""><img src="/merops/resources/red_fiss.gif" align="top" alt="Scissile bond" /></a>[\w,-]+/[\w,-]+/[\w,-]+/[\w,-]+', data)
    if res:
        s = re.sub('<a onMouseover="" onMouseout=""><img src="/merops/resources/red_fiss.gif" align="top" alt="Scissile bond" /></a>', '|', res[0])
        print(url, ' ', s)
        f.write(url + "\n")
    else:
        s = 'NA'
    k.write(s + "\n")
#
k.close()
f.close()


#input_file = open("new_urls.txt", "r")
#urls = input_file.read().splitlines()

# #PH parser
# for url in urls:
#     data = requests.get(url).text
#     id = re.sub('https://www.ebi.ac.uk/merops/cgi-bin/pepsum\?id=', '', url)
#     res_ph = re.findall('http://www.uniprot.org/uniprot/\w+', data)
#     if res_ph:
#         n_d = requests.get(res_ph[0]).text
#         ph = re.findall('Optimum pH is ([\w,\.]+)', n_d)
#         if ph:
#             print(id, ' ', ph[0])
#         else:
#             print('NA')
#     else:
#         print('NA')






