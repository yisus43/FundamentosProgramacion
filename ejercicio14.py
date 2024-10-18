# Pedir un número de dos cifras al usuario
numero = input("Ingresa un número de dos cifras: ")

# Invertir el número
'''
Esta línea invierte el número usando slicing.
La notación [::-1] significa "tomar todos los elementos de la cadena numero
pero en orden inverso". El resultado se guarda en la variable numero_invertido.
'''
numero_invertido = numero[::-1]

# Mostrar el número invertido
print("El número invertido es:", numero_invertido)
