def clasificar_numeros(a, b):
    suma = a + b
    producto = a * b
    # Crear una lista con los valores a, b, suma y producto
    valores = [a, b, suma, producto]
    # Ordenar la lista de valores
    valores_ordenados = sorted(valores)
    # Imprimir los resultados en orden
    print(f"Ordenados: {valores_ordenados}")

def obtener_numero(valor):
    while True:
        try:
            # Intenta convertir la entrada a un número entero
            return int(input(valor))
        except ValueError:
            # Si hay un error, informa al usuario y sigue intentando
            print("Por favor, ingrese un número válido.")

# Solicitar entrada del usuario para a y b
a = obtener_numero("Ingrese el valor de a: ")
b = obtener_numero("Ingrese el valor de b: ")

# Llamar a la función con los valores ingresados
clasificar_numeros(a, b)
