palindroma = lambda parola: True if(parola == "".join(reversed(parola)))else False

parola =  input("inserisci il una parola: ") 

print(palindroma(parola))