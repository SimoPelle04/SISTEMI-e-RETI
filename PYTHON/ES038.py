def divisibile(divsore, dividendo):
    divisibile = False
    if(divsore%dividendo==0):
        divisibile = True
    return divisibile

numero = int(input("INSERISCI IL NUMERO: "))
div = False
if(divisibile(numero,2)):
    print("è divisibile per 2")
    div = divisibile(numero,2)

if(divisibile(numero,3)):
    print("è divisibile per 3")
    div = divisibile(numero,3)

if(divisibile(numero,5)):
    print("è divisibile per 5")
    div = divisibile(numero,5)

if(not div):
    print("NON E DIVISIBILE PER NESSUNO DEI 3")




