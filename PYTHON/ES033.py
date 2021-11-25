import random
gara = lambda alice,bob: "pareggio"if alice == bob else "ha vinto Alice" if alice > bob else "ha vinto Bob"

alice = random.randint(1,6) 
print(f"alice: {alice}")
bob =  random.randint(1,6) 
print(f"bob: {bob}")
print(gara(alice,bob))