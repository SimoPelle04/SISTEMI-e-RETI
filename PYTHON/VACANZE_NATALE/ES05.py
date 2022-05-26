def main(): 
    f = open("file.c","r")
    c,s=0,0

    righe = f.readlines()

    print(f"Numero di righe del file: {len(righe)}")

    for riga in righe:
        if "printf" in riga:
            c+=1
        elif "//" in riga:
            s+=1

    print(f"Numero di prinf presenti: {c}")

    print(f"Numero di commenti presenti: {s}")

    f.close()

if __name__ == "__main__":
    main()