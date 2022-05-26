import PILE_CODE


def main():
    c1 = PILE_CODE.Coda()
    nEl = int(input("Quanti elementi vuoi inserire: "))

    for _ in range(0,nEl):
        elemento = input("Inserisci elemento: ")
        c1.enqueue(elemento)
    c1.print()

    p = PILE_CODE.Pila()
    for _ in range(0,nEl):
        p.push(c1.dequeue())
        
    c2 = PILE_CODE.Coda()
    for x in range(0,nEl):
        c2.enqueue(p.pop())
    c2.print()    

if __name__=="__main__":
    main() 
