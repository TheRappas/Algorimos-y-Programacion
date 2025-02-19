
	Algoritmo ejercicio_10_CambioDivisas
		
		Escribir "Ingrese la cantidad en chelines austriacos: "
		Leer chelines
		
		pesetasDeChelines <- chelines * 9.56871
		Escribir "Equivalente en pesetas: ", pesetasDeChelines
		Escribir ""
		
		Escribir "Ingrese la cantidad en dracmas griegos: "
		Leer dracmas
		
		pesetasDeDracmas <- dracmas * 0.88607
		
		francos <- pesetasDeDracmas / 20.110
		Escribir "Equivalente en francos franceses: ", francos
		Escribir ""
		
		Escribir "Ingrese la cantidad en pesetas: "
		Leer pesetasIngresadas
		
		dolares <- pesetasIngresadas / 122.499
		
		liras <- pesetasIngresadas * 10.763
		
		Escribir "Equivalente en dólares: ", dolares
		Escribir "Equivalente en liras italianas: ", liras
FinAlgoritmo

