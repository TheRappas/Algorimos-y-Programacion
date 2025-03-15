Algoritmo ejercicio_6
	Escribir "Ingrese el Año"
	Leer año
	Si año %4=0 Entonces
		Escribir "Es bisiesto"
		SiNo
			Si año %400=0 Entonces
				Escribir "Es bisiesto"
			SiNo
				Si año %100=0 Entonces
					Escribir "No es bisiesto"
				SiNo
					Escribir "No es bisiesto"
				Fin Si
			Fin Si
		Fin Si
FinAlgoritmo
