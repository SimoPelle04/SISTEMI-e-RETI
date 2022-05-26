tavola = [x*y for x in range (11) for y in range (11)]
indice1 = 0
indice2 = 11
for _ in range(1,10):
    print(tavola[indice1:indice2])
    indice1 += 11
    indice2 += 11