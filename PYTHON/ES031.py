import math

qPerfetto = lambda n: True if (not(math.sqrt(n)-int(math.sqrt(n))) and n%2 != 0) else False
    
lista = []
for x in range(1,1000):
    if qPerfetto(x):
        lista.append(x)
        
print(lista)
