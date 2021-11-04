n1 = float (input("inserisci primo numero"))
n2 = float (input("inserisci secondo numero"))
l = []
l.append(n1**2 + n2**2)
l.append((n1 + n2)**2)
l.append(n1**2 - n2**2)
l.append((n1 - n2)**2)
print(l)
