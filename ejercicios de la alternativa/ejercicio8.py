def calcular_prima(kilometros, antiguedad, num_accidentes):
    # Calcular la prima de distancia
    prima_distancia = min(kilometros * 0.01, 400)

    # Calcular la prima de antigüedad
    if antiguedad >= 4:
        prima_antiguedad = 200 + (antiguedad - 4) * 20
    else:
        prima_antiguedad = 0

    # Determinar la prima base antes de aplicar la reducción por accidentes
    prima_base = prima_distancia + prima_antiguedad

    # Reducir la prima por accidentes
    if num_accidentes == 0:
        prima_final = prima_base
    elif num_accidentes == 1:
        prima_final = prima_base / 2
    elif num_accidentes == 2:
        prima_final = prima_base / 3
    elif num_accidentes == 3:
        prima_final = prima_base / 4
    else:
        prima_final = 0  # Anular la prima para más de 3 accidentes

    return prima_final

def obtener_valores(mensaje, tipo=int):
    while True:
        try:
            entrada = tipo(input(mensaje))
            if entrada < 0:
                print("Por favor, ingrese un valor positivo.")
                continue
            return entrada
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

# Obtener el número de kilómetros recorridos
kilometros = obtener_valores("Ingrese el número total de kilómetros recorridos por el conductor este año: ")

# Obtener la antigüedad del conductor
antiguedad = obtener_valores("Ingrese el número de años de antigüedad del conductor: ")

# Obtener el número de accidentes responsables
num_accidentes = obtener_valores("Ingrese el número de accidentes este año: ")

# Calcular la prima anual
prima_anual = calcular_prima(kilometros, antiguedad, num_accidentes)

# Mostrar el resultado
print(f"La prima anual que se concederá al conductor es de {prima_anual:.2f} €.")
