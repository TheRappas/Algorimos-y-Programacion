Algoritmo ejercicio_15_PorcentajeDescuento
    
    Escribir "Ingrese el precio final pagado por el producto: "
    Leer precioFinal
    Escribir "Ingrese el precio de venta al publico (PVP): "
    Leer pvp
    
    descuento <- ((pvp - precioFinal) / pvp) * 100
    
    Escribir "El porcentaje de descuento aplicado es: ", descuento, "%"
FinAlgoritmo