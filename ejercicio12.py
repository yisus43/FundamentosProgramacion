import math

# Pedir las coordenadas del primer punto (x1, y1)
x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))

# Pedir las coordenadas del segundo punto (x2, y2)
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

# Calcular la distancia entre los dos puntos
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mostrar la distancia
print("La distancia entre los dos puntos es:", distancia)
