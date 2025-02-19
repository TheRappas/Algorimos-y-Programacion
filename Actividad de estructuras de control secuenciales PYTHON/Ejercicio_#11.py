# Entradas
nombre = input("Ingrese el nombre del trabajador: ")
horasNormales = int(input("Ingrese el número de horas normales trabajadas: "))
pagoHora = int(input("Ingrese el pago por hora normal: "))
horasExtras = int(input("Ingrese el número de horas extras trabajadas: "))
numeroHijos = int(input("Ingrese el número de hijos del trabajador: "))

# Procesos
# Sueldo base solo horas normales
sueldoBase = horasNormales * pagoHora

# Pago por horas extras
pagoHorasExtras = horasExtras * pagoHora * 1.25

# Deducciones
deduccionPagoForzoso = sueldoBase * 0.05
deduccionPoliticaHabitacional = sueldoBase * 0.02
deduccionCajaAhorro = sueldoBase * 0.07
totalDeducciones = deduccionPagoForzoso + deduccionPoliticaHabitacional + deduccionCajaAhorro

# Asignaciones fijas y por hijo
totalAsignaciones = 250000 + (173000 * numeroHijos) + 180000

# Cálculo del sueldo neto
sueldoNeto = (sueldoBase + pagoHorasExtras) - totalDeducciones + totalAsignaciones

# Salidas
print("---------- RESULTADOS ----------")
print(f"Trabajador: {nombre}")
print(f"Asignaciones totales: {totalAsignaciones} COP")
print(f"Deducciones totales: {totalDeducciones} COP")
print(f"Sueldo neto a recibir: {sueldoNeto} COP")







