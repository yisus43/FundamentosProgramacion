num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Calcular la distancia 
'''La función abs() en Python se utiliza para calcular el valor absoluto de un número. El valor absoluto de un número es su distancia a cero en la recta numérica, sin considerar su signo. Por ejemplo:

abs(5) devuelve 5.
abs(-5) también devuelve 5.
abs(0) devuelve 0.
En el contexto del código que te proporcioné, abs(num1 - num2) calcula la diferencia entre los dos números y asegura que el resultado sea siempre positivo, independientemente del orden en que se ingresen los números. Así, siempre obtendrás la "distancia" entre ellos.
'''
distancia = abs(num1 - num2)
# Mostrar la distancia
print("La distancia entre los dos números es:", distancia)