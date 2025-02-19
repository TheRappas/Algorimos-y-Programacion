import math  # Importamos la librería para usar la función sqrt (Raíz cuadrada)

# Entrada de datos
a = int(input("Ingrese la longitud del lado a: "))
b = int(input("Ingrese la longitud del lado b: "))
c = int(input("Ingrese la longitud del lado c: "))

# Cálculo del semiperímetro
s = (a + b + c) / 2

# Fórmula de Herón para calcular el área
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Mostrar el resultado
print(f"El área del triángulo es: {area:.2f}")



