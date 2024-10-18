# Calificaciones parciales
p1 = float(input("Calificación parcial 1: "))
p2 = float(input("Calificación parcial 2: "))
p3 = float(input("Calificación parcial 3: "))

# Examen final
examen_final = float(input("Calificación del examen final: "))

# Trabajo final
trabajo_final = float(input("Calificación del trabajo final: "))

# Calcular el promedio de los parciales
promedio_parciales = (p1 + p2 + p3) / 3

# Calificación final
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Mostrar la calificación final
print("Calificación final:", calificacion_final)
