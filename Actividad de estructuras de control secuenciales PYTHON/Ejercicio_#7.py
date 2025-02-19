# Entrada de datos
metros = int(input("Cantidad en metros: "))

# Cálculos
pulgadasTotales = metros * 39.27
pies = int(pulgadasTotales // 12)  # Truncamos el valor a la parte entera
pulgadas = pulgadasTotales - (pies * 12)

# Mostrar el resultado
print(f"La cantidad equivale a: {pies} Pies y {pulgadas:.2f} Pulgadas")


