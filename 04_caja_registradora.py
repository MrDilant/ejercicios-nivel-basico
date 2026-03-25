total = 0
cantidad = 0

precio = float(input("Ingresa el precio (0 para terminar): "))

while precio != 0:
    total += precio 
    cantidad += 1
    precio = float(input("Ingresa el precio (0 para terminar): "))
if cantidad > 0:
    promedio = total / cantidad
    print(f"Total: {total}")
    print(f"Cantidad: {cantidad}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron productos")
    