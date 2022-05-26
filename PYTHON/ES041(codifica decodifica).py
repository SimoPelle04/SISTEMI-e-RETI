 caratteri = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
 #RENDO LA LISTA GLOBALE MA NESSUNA FUNZIONE PUO' MODIFICARE LISTA

def codifica(s,car):
    nuovaStringa = ""
    n = int(input("Inserisci numero di criptazione: "))
    for lettera in s:
        trova = False
        k=0
        while(trova == False or k>28):
            if lettera==car[k]:
                trova=True
            else:
                k+=1
        nuovaStringa+=car[(k+n)%28]
    
    print(nuovaStringa)

def decodifica(s,car):
    nuovaStringa = ""
    n = int(input("Inserisci numero di decriptazione: "))
    for lettera in s:
        trova = False
        k=0
        while(trova == False or k>28):
            if lettera==car[k]:
                trova=True
            else:
                k+=1
        nuovaStringa+=car[(k-n)%28]
    
    print(nuovaStringa)

def main():
    CoD = input("Vuoi codificare o decodificare [C/D]:")
    frase = input("Inserisci la frase: ")
    frase = frase.upper()
    CoD = CoD.upper()
    if CoD=='C':
        codifica(frase,caratteri)
    elif CoD=='D':
        decodifica(frase,caratteri)
    else:
        print("Errore")


if __name__=="__main__":
    main()