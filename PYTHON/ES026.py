def nprimo(n):
    k=2
    continua = True
    while k<n and continua == True:
        if(n%k == 0):
            continua = False
        k=k+1
    return continua


x = int(input("inserisci il numero: "))

if nprimo(x) :
    print("il numero è primo")
else: 
    print("il numero NON è primo")