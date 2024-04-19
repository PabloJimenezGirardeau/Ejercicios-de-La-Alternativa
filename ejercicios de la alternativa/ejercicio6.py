def calcular_descuento(cantidad, es_commaq, es_bel):
    # Determinar el descuento base según la cantidad de componentes
    if 10000 <= cantidad <= 20000:
        descuento = 10
    elif 20001 <= cantidad <= 40000:
        descuento = 15
    elif cantidad > 40000:
        descuento = 20
    else:
        descuento = 0  # No hay descuento para pedidos menores de 10000 componentes

    # Ajustar el descuento según el tipo de cliente
    if es_commaq:
        descuento -= 2  # Reducir el descuento para COMMAQ
    if es_bel:
        descuento += 1  # Aumentar el descuento para BEL

    # Asegurar que el descuento no sea negativo
    if descuento < 0:
        descuento = 0

    return descuento

def preguntar_cliente():
    while True:
        try:
            respuesta_commaq = input("¿Es el cliente COMMAQ? (si/no): ").strip().lower()
            if respuesta_commaq not in ["si", "no"]:
                raise ValueError("Debe responder 'si' o 'no'.")
            respuesta_bel = input("¿Es el cliente BEL? (si/no): ").strip().lower()
            if respuesta_bel not in ["si", "no"]:
                raise ValueError("Debe responder 'si' o 'no'.")
            return respuesta_commaq == "si", respuesta_bel == "si"
        except ValueError as e:
            print(e)

def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de componentes pedidos: "))
            if cantidad < 0:
                print("Por favor, ingrese un número positivo para la cantidad de componentes.")
                continue
            return cantidad
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

# Obtener la cantidad de componentes pedidos
cantidad = obtener_cantidad()

# Preguntar si el cliente es COMMAQ o BEL
es_commaq, es_bel = preguntar_cliente()

# Calcular el descuento
descuento = calcular_descuento(cantidad, es_commaq, es_bel)

# Mostrar el porcentaje de descuento
print(f"El descuento para un pedido de {cantidad} componentes es del {descuento}%.")
