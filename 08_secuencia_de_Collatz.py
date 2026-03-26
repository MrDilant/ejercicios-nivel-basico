num = int(input("Ingrese un número: "))

pasos = 0

while num != 1:
    print(num)

    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

    
    pasos += 1



print(1)
print(f"Total de pasos: {pasos}")

