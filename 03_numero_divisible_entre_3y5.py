n = int(input("Ingresa un numero: "))
contador = 0

for i in range(1, n + 1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 and i % 5 == 0):
        print(i)
        contador += 1

print(f"Cantidad: {contador}")

