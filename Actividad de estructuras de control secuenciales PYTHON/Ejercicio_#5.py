# Entrada de datos
parcial1 = int(input("Ingrese la primera calificación parcial: "))
parcial2 = int(input("Ingrese la segunda calificación parcial: "))
parcial3 = int(input("Ingrese la tercera calificación parcial: "))
examenFinal = int(input("Ingrese la calificación del examen final: "))
trabajoFinal = int(input("Ingrese la calificación del trabajo final: "))

# Cálculos
promedioParciales = (parcial1 + parcial2 + parcial3) / 3
calificacionFinal = (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)

# Mostrar el resultado
print("La calificación final es:", calificacionFinal)



