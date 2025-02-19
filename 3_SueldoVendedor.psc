
	Algoritmo ejercicio_3_SueldoVendedor
		Escribir "Ingrese el sueldo base del vendedor: "
		Leer sueldoBase
		Escribir "Ingrese el monto de la primera venta: "
		Leer venta1
		Escribir "Ingrese el monto de la segunda venta: "
		Leer venta2
		Escribir "Ingrese el monto de la tercera venta: "
		Leer venta3
		comision <- (venta1 + venta2 + venta3) * 0.10
		total <- sueldoBase + comision
		Escribir "El total de comisiones es: ", comision
		Escribir "El sueldo total del vendedor es: ", total
FinAlgoritmo
