
	Algoritmo ejercicio_11_CalcularSalarioTrabajador
		// ENTRADAS
		Escribir "Ingrese el nombre del trabajador: "
		Leer nombre
		Escribir "Ingrese el numero de horas normales trabajadas: "
		Leer horasNormales
		Escribir "Ingrese el pago por hora normal: "
		Leer pagoHora
		Escribir "Ingrese el numero de horas extras trabajadas: "
		Leer horasExtras
		Escribir "Ingrese el numero de hijos del trabajador: "
		Leer numeroHijos
		
		// PROCESOS
		// Sueldo base solo horas normales
		sueldoBase <- horasNormales * pagoHora
		
		//Pago por horas extras 
		pagoHorasExtras <- horasExtras * pagoHora * 1.25
		
		// Deducciones
		deduccionPagoForzoso <- sueldoBase * 0.05
		deduccionPoliticaHabitacional <- sueldoBase * 0.02
		deduccionCajaAhorro <- sueldoBase * 0.07
		totalDeducciones <- deduccionPagoForzoso + deduccionPoliticaHabitacional + deduccionCajaAhorro
		
		//  Asignaciones fijas y por hijo
		totalAsignaciones <- 250000 + (173000 * numeroHijos) + 180000
		
		// Cálculo del sueldo neto
		sueldoNeto <- (sueldoBase + pagoHorasExtras) - totalDeducciones + totalAsignaciones
		
		// SALIDAS
		Escribir "---------- RESULTADOS ----------"
		Escribir "Trabajador: ", nombre
		Escribir "Asignaciones totales: ", totalAsignaciones, " COP"
		Escribir "Deducciones totales: ", totalDeducciones, " COP"
		Escribir "Sueldo neto a recibir: ", sueldoNeto, " COP"
FinAlgoritmo
