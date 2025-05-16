Students = {}
Max_Students = 10

for i in range(1, Max_Students + 1):
    print(f"Estudiante {i}:")
    Name = input("  Nombre: ")
    try:
        Value = float(input("  Nota: "))
    except ValueError:
        print("  ¡Error! Introduce una nota válida en número.")
        break

    Students[str(i)] = {
        "nombre": Name,
        "nota": Value
    }

    ContinueProcess = input("¿Desea incluir otro estudiante? (s/n): ").lower()
    if ContinueProcess != "s":
        break

Approved = []
Suspended = []
TotalValues = 0

for Student in Students.values():
    Value = Student["nota"]
    TotalValues += Value
    if Value >= 5:
        Approved.append(Student["nombre"])
    else:
        Suspended.append(Student["nombre"])

media = TotalValues / len(Students)

print("\n--- RESULTADOS ---")
print("Aprobados:", Approved)
print("Suspendidos:", Suspended)
print(f"Nota media de la clase: {media:.2f}")