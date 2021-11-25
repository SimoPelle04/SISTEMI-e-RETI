maiuscola = lambda parola: True if(parola[0]> 'A' and parola[0]< 'Z') else False

parola =  input("inserisci il una parola: ") 

print(maiuscola(parola))