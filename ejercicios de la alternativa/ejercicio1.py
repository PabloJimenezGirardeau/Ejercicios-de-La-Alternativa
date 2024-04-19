from enum import Enum

class Dia(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

def sucesor(dia):
    # Calcular el próximo día sumando 1 y tomando el módulo 7 para volver a Lunes después de Domingo
    return Dia((dia.value + 1) % 7)

# Función para obtener el día desde un input de usuario
def obtener_dia():
    while True:
        try:
            # Corregir la llamada a upper para que se ejecute correctamente
            dia = input("Ingrese el día actual (en mayúsculas, e.g.,LUNES, MARTES...): ").upper()
            dia_actual = Dia[dia]
            return dia_actual
        except KeyError:
            print("No ingresó un día válido. Por favor, intente de nuevo.")

# Obtener día desde input
dia_actual = obtener_dia()
print("Hoy es:", dia_actual.name)

# Calcular el sucesor
dia_siguiente = sucesor(dia_actual)
print("Mañana será:", dia_siguiente.name)


