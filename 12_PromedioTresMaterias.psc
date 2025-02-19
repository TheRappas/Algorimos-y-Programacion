
	Algoritmo EJERCICIO_12_PromedioTresMaterias
		
		// MATEMÁTICA
		Escribir "Ingrese la nota del examen de Matematica: "
		Leer examMat
		Escribir "Ingrese las tres notas de tareas de Matematica: "
		Leer t1Mat
		Leer t2Mat
		Leer t3Mat
		
		promTareasMat <- (t1Mat + t2Mat + t3Mat) / 3
		finalMat <- examMat * 0.90 + promTareasMat * 0.10
		
		// FÍSICA
		Escribir "Ingrese la nota del examen de Fisica: "
		Leer examFis
		Escribir "Ingrese las dos notas de tareas de Fisica: "
		Leer t1Fis
		Leer t2Fis
		
		promTareasFis <- (t1Fis + t2Fis) / 2
		finalFis <- examFis * 0.80 + promTareasFis * 0.20
		
		// QUÍMICA
		Escribir "Ingrese la nota del examen de Quimica: "
		Leer examQuim
		Escribir "Ingrese las tres notas de tareas de Quimica: "
		Leer t1Quim
		Leer t2Quim
		Leer t3Quim
		
		promTareasQuim <- (t1Quim + t2Quim + t3Quim) / 3
		finalQuim <- examQuim * 0.85 + promTareasQuim * 0.15
		
		// PROMEDIO GENERAL
		promedioGeneral <- (finalMat + finalFis + finalQuim) / 3
		
		// SALIDAS
		Escribir "---------- RESULTADOS ----------"
		Escribir "Promedio final en Matematica: ", finalMat
		Escribir "Promedio final en Fisica: ", finalFis
		Escribir "Promedio final en Quimica: ", finalQuim
		Escribir "Promedio general de las tres materias: ", promedioGeneral
FinAlgoritmo

