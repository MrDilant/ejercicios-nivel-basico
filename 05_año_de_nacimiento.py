nacimiento = int(input("Ingresa tu año de nacimiento: "))

for año in range(1900,2025):
    edad = año - nacimiento
    if edad >= 0 and edad % 5 == 0:
        print(f"Año: {año}- Edad: {edad}")
