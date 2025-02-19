# Entrada de datos
horas = int(input("Horas trabajadas: "))
precio = int(input("Precio de hora: "))

# Cálculo del salario y descuentos
salario = horas * precio
descuento = salario * 0.20
sueldoTotal = salario - descuento

# Mostrar los resultados
print(f"Salario base es: {salario}")
print(f"Descuento por impuestos: {descuento}")
print(f"El salario neto es: {sueldoTotal}")






