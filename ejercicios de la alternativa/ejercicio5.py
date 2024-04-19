def calcular_descuento(num_ninos, precio_total):
    # Determinar el porcentaje de descuento según el número de niños
    if num_ninos == 2:
        descuento_porcentaje = 10
    elif num_ninos == 3:
        descuento_porcentaje = 15
    elif num_ninos >= 4:
        descuento_porcentaje = 18 + (num_ninos - 4) * 1
    else:
        # No hay descuento para menos de 2 niños
        descuento_porcentaje = 0
    
    # Calcular el importe del descuento
    descuento_importe = precio_total * (descuento_porcentaje / 100)
    
    return descuento_importe, descuento_porcentaje

def calcular_precio_final(precio_total, descuento_importe):
    # Calcular el precio final después de aplicar el descuento
    return precio_total - descuento_importe

def obtener_datos():
    while True:
        try:
            num_ninos = int(input("Ingrese el número de niños en la familia: "))
            if num_ninos < 0:
                print("No se pueden ingresar números negativos para la cantidad de niños.")
                continue
            elif num_ninos < 2:
                print("No hay descuento aplicable para menos de 2 niños.")
                continue
            precio_total = float(input("Ingrese el precio total de las entradas: "))
            if precio_total < 0:
                print("El precio debe ser un valor positivo.")
                continue
            return num_ninos, precio_total
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

# Obtener el número de niños y el precio total de las entradas
num_ninos, precio_total = obtener_datos()

# Calcular el descuento y el porcentaje aplicado
descuento_importe, descuento_porcentaje = calcular_descuento(num_ninos, precio_total)

# Calcular el precio final
precio_final = calcular_precio_final(precio_total, descuento_importe)

# Mostrar el importe del descuento, el porcentaje de descuento y el precio final
print(f"El descuento es del {descuento_porcentaje}% y el importe del descuento es de {descuento_importe:.2f} €.")
print(f"El precio final es {precio_final:.2f} €.")


