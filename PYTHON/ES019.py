import math
ax = float (input("inserisci x1: "))
ay = float (input("inserisci y1: "))
bx = float (input("inserisci x2: "))
by = float (input("inserisci y2: "))
tupla = (ax,ay,bx,by)

distanza = math.sqrt((tupla[0]-tupla[2])**2 +  (tupla[1]-tupla[3])**2)
print(f"La distanza tra a e b è di {distanza}")