nome,cognome,data=input("Inserisci il nome : "),input("Inserisci il cognome : "),input("Inserisci la data (giorno/mese/anno) : ")
dizionario={"nome" : nome ,"cognome" : cognome ,"data" : data }
testo=open("./file.txt","w")

str=dizionario["cognome"]+" "+dizionario["nome"]+" "+dizionario["data"]
testo.write(str)