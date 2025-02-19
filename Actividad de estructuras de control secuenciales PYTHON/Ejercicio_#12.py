
# MATEMÁTICA
examMat = int(input("Ingrese la nota del examen de Matemática: "))
t1Mat = int(input("Ingrese la primera nota de tareas de Matemática: "))
t2Mat = int(input("Ingrese la segunda nota de tareas de Matemática: "))
t3Mat = int(input("Ingrese la tercera nota de tareas de Matemática: "))

promTareasMat = (t1Mat + t2Mat + t3Mat) / 3
finalMat = examMat * 0.90 + promTareasMat * 0.10

# FÍSICA
examFis = int(input("Ingrese la nota del examen de Física: "))
t1Fis = int(input("Ingrese la primera nota de tareas de Física: "))
t2Fis = int(input("Ingrese la segunda nota de tareas de Física: "))

promTareasFis = (t1Fis + t2Fis) / 2
finalFis = examFis * 0.80 + promTareasFis * 0.20

# QUÍMICA
examQuim = int(input("Ingrese la nota del examen de Química: "))
t1Quim = int(input("Ingrese la primera nota de tareas de Química: "))
t2Quim = int(input("Ingrese la segunda nota de tareas de Química: "))
t3Quim = int(input("Ingrese la tercera nota de tareas de Química: "))

promTareasQuim = (t1Quim + t2Quim + t3Quim) / 3
finalQuim = examQuim * 0.85 + promTareasQuim * 0.15

# PROMEDIO GENERAL
promedioGeneral = (finalMat + finalFis + finalQuim) / 3

# SALIDAS
print("---------- RESULTADOS ----------")
print(f"Promedio final en Matemática: {finalMat}")
print(f"Promedio final en Física: {finalFis}")
print(f"Promedio final en Química: {finalQuim}")
print(f"Promedio general de las tres materias: {promedioGeneral}")







