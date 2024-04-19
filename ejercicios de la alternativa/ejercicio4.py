def calcular_media_y_evaluacion(notas):
    # Calcular la media de las notas
    media = sum(notas) / len(notas)
    
    # Determinar la evaluación basada en la media
    if media > 15:
        evaluacion = "Alumno con talento"
    elif 12 <= media <= 15:
        evaluacion = "Con capacidad"
    else:
        evaluacion = "Debe reorientarse"
    
    return media, evaluacion

def obtener_notas():
    notas = []
    for i in range(1,5):  # Suponiendo que siempre son cuatro notas
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i} (de 0 a 20): "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return notas

# Obtener las notas del alumno
notas_alumno = obtener_notas()

# Calcular la media y la evaluación
media, evaluacion = calcular_media_y_evaluacion(notas_alumno)

# Mostrar los resultados
print(f"La media del alumno es: {media:.2f}")
print(f"Evaluación: {evaluacion}")
