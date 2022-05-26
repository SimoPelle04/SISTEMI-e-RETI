def main():
    f = open("./medals.csv", "r") 
    righe = f.readlines()
    medaglie = {"Gold" : 0, "Silver" : 0, "Bronze" : 0}

    for riga in righe:
        x = riga.split(",")
        nazione = x[8]
        #print(nazione)
        if(nazione == "Italy"):
            #print(x)
            #ptint(x[0])
            tipo = x[0]
            medaglie [tipo] +=1

    print(medaglie)
    f.close()

if __name__=="__main__":
    main() 