
saldo = 1000000

while True:
    print("CAJERO")
    print("1. Consignar")
    print("2. Retirar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("Monto a consignar: "))
        if monto > 0:
            saldo += monto 
            print("Consignación exitosa")
        else:
            print(("Monto inválido"))


    
    elif opcion == "2":
        monto = float(input("Monto a retirar: "))
    
        if monto > saldo:
            print("No tiene saldo suficiente")
    
        elif monto <= 0:
            print("Monto inválido")
    
        else:
            saldo -= monto 
            print("Retiro exitoso")

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print

        
print(f"Saldo actual: ${saldo}")