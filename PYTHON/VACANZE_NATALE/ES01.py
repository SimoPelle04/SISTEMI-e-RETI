
lista = [1,2,33,2,33,4,4]
print(lista)

def Elimina():
    for x in lista:
        if lista.count(x)>1:
            lista.remove(x)
            Elimina()
    return lista

Elimina()
print(lista)
    