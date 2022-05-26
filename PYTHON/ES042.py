def nomeAsterischi (nome):
    conta = len(nome)
    return nome[0] + (conta-1)*"*"

def main():
    f = open("./file.csv","w")
    ancora = "si"

    while ancora == "si":
        nome = input("Inserisci nome alunno: ")
        voto = int(input("Inserisci voto: "))
        nome2 = nomeAsterischi(nome)
        ancora = input("ce ne sono ancora: (si/no): ")
        f.write(f"{nome2}, {voto} \n")

    f.close()

if __name__=="__main__":
    main()