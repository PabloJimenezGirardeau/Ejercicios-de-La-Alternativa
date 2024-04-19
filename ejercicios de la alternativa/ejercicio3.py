def calcular_descuento(importe):
    # Comprobar el rango del importe y aplicar el descuento correspondiente
    if 100 <= importe <= 500:
        descuento = importe * 0.05  # Aplicar un descuento del 5% para compras entre 100 y 500 euros
    elif importe > 500:
        descuento = importe * 0.08  # Aplicar un descuento del 8% para compras mayores a 500 euros
    else:
        descuento = 0  # No aplicar descuento si el importe es menor de 100 euros
    return descuento  # Devolver el valor del descuento calculado

def obtener_importe(prompt):
    while True:
        try:
            # Solicitar al usuario el importe de la compra
            importe = float(input(prompt))
            if importe >= 0:
                return importe  # Retornar el importe si es un número positivo
            else:
                print("Por favor, ingrese un importe positivo.")  # Pedir de nuevo si el número no es positivo
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Manejar el error si la entrada no es un número

# Solicitar el importe de la compra
importe_compra = obtener_importe("Ingrese el importe de la compra: ")

# Calcular el descuento basado en el importe de la compra
descuento = calcular_descuento(importe_compra)

# Mostrar el descuento aplicado, formateando la salida para incluir dos decimales
print(f"El descuento aplicado es: {descuento:.2f} €")
