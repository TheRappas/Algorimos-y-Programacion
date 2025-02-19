
	Algoritmo ejercicio_16_Gasolinera
		// Dato fijo
		precioLitro <- 50000
		
		Escribir "Ingrese la cantidad de galones surtidos: "
		Leer galones
		
		litros <- galones * 3.785
		
		totalAPagar <- litros * precioLitro
		
		Escribir "---------- RESULTADOS ----------"
		Escribir "Litros surtidos: ", litros
		Escribir "Total a pagar (COP): ", totalAPagar
	Finalgoritmo
