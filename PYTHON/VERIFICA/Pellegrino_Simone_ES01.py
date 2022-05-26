import random

def spostamento_rand():
    n = random.randint(0,1) 
    if(n==0):
        spostamento = -1
    else:
        spostamento = 1

    return spostamento

secondi = 60*60*24*5
somma = 0
spostamenti = [spostamento_rand() for _ in range(1,secondi)]

for spostamento in spostamenti:
    somma += spostamento
print(f"spostamento: {somma}")