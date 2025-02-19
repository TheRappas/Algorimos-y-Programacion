


# Entrada de datos
mujeres = int(input("Número de mujeres: "))
hombres = int(input("Número de hombres: "))

# Cálculos
total_estudiantes = mujeres + hombres
pormujeres = (mujeres / total_estudiantes) * 100
porhombres = (hombres / total_estudiantes) * 100

# Mostrar los resultados
print("Porcentaje de hombres:", porhombres, "%")
print("Porcentaje de mujeres:", pormujeres, "%")

