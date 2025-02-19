
	Algoritmo ejercicio_9_CalcularSalario
		Escribir "Horas Trabajadas:"
		Leer Horas
		Escribir "Precio De Hora:"
		Leer Precio
		
		Salario<-Horas * Precio
		Descuento<- Salario * 0.20
		SueldoTotal<-Salario - Descuento 
		
		Escribir "Salario base es:",Salario
		Escribir "Descuento por impuestos:",Descuento
		Escribir "El salario neto es:", SueldoTotal
FinAlgoritmo
