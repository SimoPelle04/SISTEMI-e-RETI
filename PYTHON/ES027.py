def nprimo(n):
    k=2
    continua = True
    while k<n and continua == True:
        if(n%k == 0):
            continua = False
        k=k+1
    return continua

lista = []
n_primi = 0
for x in range(2,1000):
    if nprimo(x):
        lista.append(x)
        n_primi += 1
        
print(f"Nei primi 1000 numeri ci sono {n_primi} numeri")
print(lista)


