import itertools
import random

lista = [1,2,3,4,5]

permutazioni = list(itertools.permutations(lista))

perRand = random.randint(0, len(lista)+1)
print(permutazioni[perRand])

