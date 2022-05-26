classi = {"4Arob""3Brob""2Achi""3Ainf}
indirizzi = {"rob":"robotica","inf":"informatica","chi":"chimica"}
for classe in classi:
    indirizzo = indirizzi[classe[-3:]]
    print(f"La classe {classe} è dell' indirizo {indirizzo}")