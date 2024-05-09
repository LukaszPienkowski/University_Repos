## Function returning every prime number from 0 to n

n = int(input("Enter the number of prime numbers sequence: ")) #Input liczby wyrazów ciągu liczb pierwszych
a = 2 #Dolne ograniczenie liczb pierwszych; zaczynają się od 2
while n!=0: #Początek pętli 
    for i in range(2,a): 
        if a%i == 0: #Sprawdzenie dzielnika; warunek dla liczb pierwszych
            break
    else:
        print(a,end=", ") #Output wyrazów licz pierwszych
        n -= 1 #Wymóg do zatrzymania podawania liczb
    a += 1 #Kolejny wymóg, bez tego równania otrzymalibyśmy same dwójki
