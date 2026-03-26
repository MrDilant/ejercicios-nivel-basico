filas = int(input("Ingrese un número: "))

if filas > 0:
    for i in range(1, filas + 1):
        cantidad = 2 * i - 1

        for j in range(cantidad):
            print("*", end="")


        print()

else:
    print("Ingresa un número positivo")