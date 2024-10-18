import math

# Pedir un número al usuario
numero = float(input("Ingresa un número: "))

# Calcular la raíz cuadrada y la raíz cúbica
raiz_cuadrada = math.sqrt(numero)
raiz_cubica = numero ** (1/3)

# Mostrar los resultados
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("La raíz cúbica de", numero, "es:", raiz_cubica)
