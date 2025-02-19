# Entrada de datos para chelines a pesetas
chelines = int(input("Ingrese la cantidad en chelines austriacos: "))
pesetasDeChelines = chelines * 9.56871
print(f"Equivalente en pesetas: {pesetasDeChelines}\n")

# Entrada de datos para dracmas a francos franceses
dracmas = int(input("Ingrese la cantidad en dracmas griegos: "))
pesetasDeDracmas = dracmas * 0.88607
francos = pesetasDeDracmas / 20.110
print(f"Equivalente en francos franceses: {francos}\n")

# Entrada de datos para pesetas a dólares y liras italianas
pesetasIngresadas = float(input("Ingrese la cantidad en pesetas: "))
dolares = pesetasIngresadas / 122.499
liras = pesetasIngresadas * 10.763

# Mostrar resultados
print(f"Equivalente en dólares: {dolares}")
print(f"Equivalente en liras italianas: {liras}")






