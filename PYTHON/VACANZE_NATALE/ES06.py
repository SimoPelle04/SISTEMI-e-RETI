def main():    
    f = open("covid-19_gen1.txt", "r")

    righe = f.readlines()
    f.close()
    lista = ["A","T","C","G"]
    contA,contT,contC,contG = 0,0,0,

    for riga in righe:
        for x in lista:
            if(x == "A"):
                contA += riga.count(x)
            elif(x == "T"):
                contT += riga.count(x)
            elif(x == "C"):
                contC += riga.count(x)
            elif(x == "G"):
                contG += riga.count(x)

    dizionario= {lista[0]: contA, lista[1]:contT,lista[2]:contC,lista[3]:contG}
    print(dizionario)

if __name__ == "__main__":
    main()                                                       