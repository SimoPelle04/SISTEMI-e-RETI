palindroma = lambda parola: True if(parola == "".join(reversed(parola)))else False
maiuscola = lambda parola: True if(parola[0]> 'A' and parola[0]< 'Z') else False

parole = ["OTTO", "ciao", "itopinonavevanonipoti", "Miao"]
maiuscole = []
palindrome = []

for parola in parole:
    if(palindroma(parola)):
        palindrome.append(parola)
    if(maiuscola(parola)):
        maiuscole.append(parola)
#maiuscole = [parola for parola in parole if maiuscola(parola)]
#palindrome= [parola for parola in parole if palindroma(parola)]
print(maiuscole)
print(palindrome)