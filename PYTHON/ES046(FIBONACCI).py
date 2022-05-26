def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

def main():
    num = int(input("Inserisci il numero di valori che vuoi vedere: "))

    for x in range(1, num+1):
        print(fibonacci(x))


if __name__=="__main__":
    main()