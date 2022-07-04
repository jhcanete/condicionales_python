# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
x = numero_1
y = numero_2

if x > y:
    print("x =", x, ("es mayor a =", y))
else:
    print("x =", x, ("es menor a =",y))

   

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if x > 0:
    print("es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if x > 0 < 100:
    print("x esta entre cero y 100")


# Verifique si el numero_1 es menor a 10 o el numero_2
if x < 10:
    print("x es menor a 10")
if y < 10:
    print("y es menor a 10")



# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if x > -2:
    print("x es mayor a -2")
if y > -2:
    print("y es mayor a -2")
    