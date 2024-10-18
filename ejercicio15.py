# Pedir al usuario que ingrese dos números
A = float(input("Ingresa el valor de A: "))
B = float(input("Ingresa el valor de B: "))

# Intercambiar los valores de A y B
temp = A  # Guardar el valor de A en una variable temporal
A = B     # Asignar el valor de B a A
B = temp  # Asignar el valor guardado de A a B

# Mostrar los resultados
print("El nuevo valor de A es:", A)
print("El nuevo valor de B es:", B)
