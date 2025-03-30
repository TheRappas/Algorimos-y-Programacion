def es_numero_perfecto(numero):
    suma_divisores = 0  
    for i in range(1, numero):
        if numero % i == 0: 
            suma_divisores += i
numero = int(input("Ingresa un número entero positivo: "))
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")