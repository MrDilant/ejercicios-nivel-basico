while True:
    contraseña = input("Ingrese su contraseña: ")


    tiene_numero = False
    tiene_mayus = False


    for c in contraseña:
        if c.isdigit():
            tiene_numero = True
        if c.isupper():
            tiene_mayus = True

    
    if len(contraseña) >= 8 and tiene_numero and tiene_mayus:
        print("Contraseña válida")
        break
    
    else:
        if len(contraseña) < 8:
            print("Debe tener 8 carácteres")
        
        if not tiene_numero:
            print("Debe tener al menos un número")
        
        if not tiene_mayus:
            print("Debe tener al menos una mayúscula")