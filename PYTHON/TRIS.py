def griglia(celle):
    for cella in celle:
        if ((int(cella)+1)%3 != 0):
            print(f"{celle[cella]} |",end = " ")
        else:
            print(f" {celle[cella]} \n ------- \n")
            
def cellaVuota(mossa,celle):
    vuota = False
    if(celle[mossa] == " "):
        vuota = True
    return vuota


celle = {"0":" ","1":" ", "2":" ", "3":" ", "4":" ", "5":" ", "6":" ", "7":" ", "8":" "}
partitaFinita = False

giocatore1 = input("Nome Giocatore 1: ")
giocatore2 = input("Nome Giocatore 2: ")

while(not partitaFinita):

    mossa = input(f"Turno di {giocatore1}: ")
    while(not cellaVuota(mossa, celle) or int(mossa) > 8 or int(mossa) < 0):
        mossa = input(f"Cella occupata, turno di {giocatore1}: ")

    celle[mossa] = "X"

    griglia(celle)
    
    #controlla win
    mossa = input(f"Turno di {giocatore2}: ")
    while(not cellaVuota(mossa, celle)):
        mossa = input(f"Cella occupata, turno di {giocatore2}: ")
    
    celle[mossa] = "O"

    griglia(celle)
    #controllo win



