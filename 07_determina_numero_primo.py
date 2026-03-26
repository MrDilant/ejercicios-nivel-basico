num = int(input("Ingresa tu numero: "))

es_primo = True

if num <= 1:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

if es_primo: 
    print("El número es primo")
else:
    print("El número NO es primo")


print(f"Primos desde 2 hasta {num}")

for n in range(2,num + 1):
    es_primo = True

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(n)