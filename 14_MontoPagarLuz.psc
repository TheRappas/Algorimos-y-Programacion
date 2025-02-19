
	Algoritmo ejercicio_14_MontoPagarLuz
		
		Escribir "Ingrese la lectura anterior del medidor (kWh): "
		Leer lecturaAnterior
		Escribir "Ingrese la lectura actual del medidor (kWh): "
		Leer lecturaActual
		Escribir "Ingrese el costo por kilovatio (COP/kWh): "
		Leer costoKwh
		
		consumo <- lecturaActual - lecturaAnterior
		montoAPagar <- consumo * costoKwh
		
		Escribir "---------- RESULTADOS ----------"
		Escribir "Consumo del mes (kWh): ", consumo
		Escribir "Monto total a pagar (COP): ", montoAPagar
FinAlgoritmo
