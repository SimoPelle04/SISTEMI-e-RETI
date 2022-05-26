
operazione = int (input("quale operazione vuoi fare?(0:somma,2:sottrazione,3:moltiplicazione,3:divisione): "))
if (operazione>3):
    print("hai inserito un numero non corretto")
else:

    x1 = float (input("inserisci il primo elemento: "))
    x2 = float (input("inserisci il primo elemento: "))

    if(operazione == 0):
        risultato = x1+x2
    elif (operazione == 1):
        risultato = x1-x2
    elif (operazione == 2):
        risultato = x1*x2
    else:
        risultato = x1/x2

    print(f"{risultato}")