n = int(input('Inserire il numero: '))

def fattoriale(n):
        if n==0:
            return 1
        else:
            return n*fattoriale(n-1)

def main():
    print ('Il fattoriale è', fattoriale(n))

if __name__=="__main__":
    main()