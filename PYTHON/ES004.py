#slicing
stringa = "Classe quarta a robotica"
print (f"{stringa}")
print (f"Il primo carattere è {stringa[0]}")
print (f"Il primo carattere è {stringa[-1]}")
#taglio una parte della stringa dall' elemento 0  al 6 escluso
print (stringa[0:6])
#prendo da elemento 6 fino alla fine 
print (stringa[6:])
#prendo elementi da 2 a 14 saltando di due in due
print (stringa[2:14:2])
#inverto la stringa perche prendo tutti gli elementi ma parto dall ultimo e salto di meno 1
print (stringa[::-1])

#stringa[15] = "b" #non si può fare perche in python le stringhe sono elementi immpotabili
stringaNuova = stringa[0:14] + "B" +  stringa[15:] 
print (f"{stringaNuova}")