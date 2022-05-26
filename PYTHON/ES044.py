#es chiedere stringa utente,
#   FACCIO UN CICLO SULLA STRINGA IN CUI PRENDO IN COSIDERAZIONE SOLO LE PARENTESI(){}[]
#   SE TROVO PARENTESI APERTA FACCIO PUSH, SE TROVO PARENTESI CHIUSA FACCIO POP


def main():
    s = input("Inserisci stringa: ")
    pila = []
    for k in (len(stringa)):
        if(s[k] == "(" and s[k] == "[" and s[k] == "{"):
            pila.append(stringa[k])
        if( and s[k] == ")" and s[k] == "]" and s[k] == "}")
            e = pila.pop()
            if(e == "("):
                if(s[k] != ")"):
                    print("Errore")
                    k= le
            if(e == "["):
                if(s[k] != "]"):
                    print("Errore")
            if(e == "{"):
                if(s[k] != "}"):
                    print("Errore")


if __name__=="__main__":
    main()