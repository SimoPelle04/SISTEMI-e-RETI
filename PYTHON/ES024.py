lista = []
ancora = 'si'
while ancora == 'si':
    lista.append(int(input("inserisci un elemento: ")))
    ancora = input("ci sono ancora numeri?(si/no)")

print(lista)