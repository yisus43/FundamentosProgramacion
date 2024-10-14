'''
Un vendedor recibe un sueldo base mas de un 10% extra por comision de sus ventas,el vendedor desea
saber cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes
y el total que recibira en el mes tomando en cuenta su sueldo base y comisiones

Entradas:
    sbase:interger
    v1:interger
    v2:interger
    v3:interger
Salidas:
    comision
'''
print("Un vendedor recibe un sueldo base mas de un 10 extra por comision de sus ventas el vendedor desea saber cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibira en el mes tomando en cuenta su sueldo base y comisiones")

sbase=input("Ingresa el sueldo:")
sbase=int(sbase)
v1=input("Ingresa el precio de la venta 1 :")
v1=int(v1)
v2=input("Ingresa el precio de la venta 2 :")
v2=int(v2)
v3=input("Ingresa el precio de la venta 3 :")
v3=int(v3)
comision=v1*0.1+v2*0.1+v3*0.1

print("La comision por ventas es:",comision)
print("Sueldo total:",sbase+comision)
