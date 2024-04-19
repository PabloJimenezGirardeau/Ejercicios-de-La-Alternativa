def calcular_precio_por_alumno(num_alumnos, num_dias):
    # Determinar el costo del trayecto por alumno
    if num_alumnos <= 25:
        costo_trayecto = 67.30
    else:
        costo_trayecto = 61.00

    # Determinar el costo de alojamiento por día
    if num_alumnos < 30:
        costo_alojamiento = 4.75
    elif 30 <= num_alumnos <= 35:
        costo_alojamiento = 4.00
    else:
        costo_alojamiento = 3.50

    # Costo de la comida por día
    costo_comida = 3.50

    # Calcular el costo total por alumno
    costo_total_por_alumno = (costo_trayecto + (costo_comida + costo_alojamiento) * num_dias)
    return costo_total_por_alumno

def calcular_precio_total(num_alumnos, costo_por_alumno):
    return num_alumnos * costo_por_alumno

def obtener_entrada_numerica(mensaje, tipo=float):
    while True:
        try:
            entrada = tipo(input(mensaje))
            if entrada <= 0:
                raise ValueError("Por favor, ingrese un número positivo.")
            return entrada
        except ValueError as e:
            print(e)

# Obtener la cantidad de alumnos y el número de días del viaje
cantidad_alumnos = obtener_entrada_numerica("Ingrese la cantidad de alumnos participantes: ", int)
dias_viaje = obtener_entrada_numerica("Ingrese la cantidad de días del viaje: ", int)

# Calcular el costo por alumno
costo_por_alumno = calcular_precio_por_alumno(cantidad_alumnos, dias_viaje)

# Calcular el costo total del viaje
costo_total_viaje = calcular_precio_total(cantidad_alumnos, costo_por_alumno)

# Mostrar resultados
print(f"El precio por alumno para el viaje es de {costo_por_alumno:.2f} €.")
print(f"El precio total para el viaje es de {costo_total_viaje:.2f} €.")
