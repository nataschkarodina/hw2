n = 20
k = 1
w = 20
weigth = w
for i in range (1, 21):
    print ('i', i)
    current_weight = 2*weigth*0.9
    weigth = current_weight
    k = 2**(i)
    print ('k', k)
print ('result')
print ('weight', weigth)
print ('number', k)
