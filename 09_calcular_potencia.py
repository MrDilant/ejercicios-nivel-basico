base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = 1

for i in range(1, exponente + 1):
    resultado = resultado * base
    print(f"Paso {i}: {resultado}")


print(f"Resultado final: {resultado}")

