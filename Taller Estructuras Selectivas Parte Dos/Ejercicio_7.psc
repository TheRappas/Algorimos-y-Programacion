Algoritmo Ejercicio_7
	escribir "Ingrese un numero entero "
	leer numero 
	si numero <= 1 Entonces
		escribir"No es primo"
	sino 
		es_Primo <- verdadero
		para i <- 2 hasta numero - 1 Hacer
			
			si numero mod i = 0 Entonces
				es_Primo <- falso
			FinSi
		finpara
		
		si es_Primo Entonces
			escribir"Es primo"
		SiNo
			escribir"No es primo"
		FinSi
	finsi
	
FinAlgoritmo
