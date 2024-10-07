'''
2.Programa que calcule el area y el perimetro de un rectangulo
a partir de su base y su altura
Entradas:
    base=interger
    altura:interger
Salidas:
    perimetro:interger
    area:interger
Analisis:
    se requiere calcular con las formulas para area y perimetro
'''
#input siempre regresa un string
#para tratarlo como otro dato se debe convertir
print("Programa que calcula area y perimetro de un rectangulo")
base=input("Escribe la base del rectangulo: ")
base=int(base)
altura=input("Escribe la altura del rectangulo: ")
altura=int(altura)
area=base*altura
## otra forma de la base por la altura      perimetro=base+base+altura+altura
perimetro=(base+altura)*2   ##aca los operadores siguen una jerarquia
## print("El perimetro del rectangulo es "+str(area))
print("El perimetro del rectangulo es ",area)
print("El perimetro del rectangulo es ",perimetro)