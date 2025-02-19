
	Algoritmo ejercicio_8_AreaTriangulo
		
		Escribir "Ingrese la longitud del lado a: "
		Leer a
		Escribir "Ingrese la longitud del lado b: "
		Leer b
		Escribir "Ingrese la longitud del lado c: "
		Leer c
		//CALCULAMOS EL SEMIPERIMETRO
		s <- (a + b + c) / 2
		//FORMULA DE HERON
		area <- Raiz(s * (s - a) * (s - b) * (s - c))
		
		Escribir "El área del triángulo es: ", area
FinAlgoritmo
