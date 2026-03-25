secreto = 42
intentos = 0

num = int(input("Adivina el número: "))

while num != secreto:
    if num < secreto:
        print("Es mayor")
    else:
        print("Es menor")

    intentos += 1
    num = int(input("Intenta de nuevo: "))

intentos += 1
print("Correcto")
print(f"Intentos: {intentos}")
