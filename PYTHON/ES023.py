parole = ["ciao","topo","pappagallo","gg"]
parolaPiuLunga = parole[0]

for parola in parole:
    if(len(parolaPiuLunga) < len(parola)):
        parolaPiuLunga = parola
    
print(parolaPiuLunga)