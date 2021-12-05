import random

f = open("./file.txt","w")
bob = str([random.randint(1,6) for _ in range(1,11)])
alice = str([random.randint(1,6) for _ in range(1,11)])
print(f"{alice}")
print(f"{bob}")

for n in range(1,30,3):
    f.write(alice[n])
    f.write(",")
    f.write(bob[n])
    f.write("\n")
f.close()