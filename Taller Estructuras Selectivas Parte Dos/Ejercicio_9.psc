Algoritmo Ejercicio_9
	Escribir "Ingrese número entero: "
    Leer numero
	
    normal <- numero
    reverso <- 0
    cantidad_digitos <- Longitud(ConvertirATexto(numero))
	
    Para i <- 1 Hasta cantidad_digitos Hacer
        digito <- numero mod 10
        reverso <- reverso * 10 + digito
        numero <- trunc(numero / 10)
    FinPara
	
    Si normal = reverso Entonces
        Escribir "Es palíndromo"
    Sino 
        Escribir "No es palíndromo"
    FinSi
	
FinAlgoritmo
