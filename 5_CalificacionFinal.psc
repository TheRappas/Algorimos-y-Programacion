
	Algoritmo ejercicio_5_CalificacionFinal
		Escribir "Ingrese la primera calificación parcial: "
		Leer parcial1
		Escribir "Ingrese la segunda calificación parcial: "
		Leer parcial2
		Escribir "Ingrese la tercera calificación parcial: "
		Leer parcial3
		Escribir "Ingrese la calificación del examen final: "
		Leer examenFinal
		Escribir "Ingrese la calificación del trabajo final: "
		Leer trabajoFinal
		promedioParciales <- (parcial1 + parcial2 + parcial3) / 3
		calificacionFinal <- (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)
		Escribir "La calificación final es: ", calificacionFinal
FinAlgoritmo
