total_consumidores = 0
total_mujeres_menores = 0
total_hombres_edad_20_25_sin_aguardiente = 0
suma_edades_cerveza = 0
consumidores_cerveza = 0
consumidores_whisky = 0
total_encuestados = 0
continuar = "S"
while continuar.upper() == "S":
    print("\nEncuesta:")
    consume_licor = input("¿Consume licor? (Sí/No): ").strip().lower()
    if consume_licor == "sí" or consume_licor == "si":
        total_consumidores += 1
        licor_preferido = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo == "F" and edad < 18:
            total_mujeres_menores += 1
        if sexo == "M" and licor_preferido != 1 and 20 <= edad <= 25:
            total_hombres_edad_20_25_sin_aguardiente += 1
        if licor_preferido == 3:  # Cerveza
            consumidores_cerveza += 1
            suma_edades_cerveza += edad
        if licor_preferido == 5:  # Whisky
            consumidores_whisky += 1
    total_encuestados += 1
    continuar = input("¿Desea continuar con la encuesta? (S/N): ").strip()
promedio_edad_cerveza = suma_edades_cerveza / consumidores_cerveza if consumidores_cerveza > 0 else 0
porcentaje_whisky = (consumidores_whisky / total_encuestados) * 100 if total_encuestados > 0 else 0
print("\nResultados de la encuesta:")
print(f"Total de personas encuestadas que consumen licor: {total_consumidores}")
print(f"Total de mujeres menores de edad: {total_mujeres_menores}")
print(f"Total de hombres entre 20 y 25 años que no consumen aguardiente: {total_hombres_edad_20_25_sin_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky:.2f}%")