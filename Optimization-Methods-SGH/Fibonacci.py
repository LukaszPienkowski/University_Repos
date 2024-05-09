    ## Function calculating n Fibonaccci number

def fib(n): #Funkcja ogólna
    if n == 0:
        return 0 #Określenie wartości dla F0
    elif n == 1:
        return 1 #Określenie wartości dla F1
    else:
        return fib(n-2) + fib(n-1) #Funkcja obliczająca wartość Fn dla n > 1

n = int(input("Enter the number of the Fibonacci sequence: ")) #Input do deklaracji wartości n
print(fib(n)) #Output dla n-tego wyrazu ciągu 