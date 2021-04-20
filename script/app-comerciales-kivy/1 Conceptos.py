# Tipos de comentarios
# Utilizando el símbolo de la almohadilla o 'sharp' # para comentar una linea
"""
Utilizando 3 comillas dobles al principio
de una serie de lineas
a comentar
"""
# Variables
"""
Las variables en python deben comenzar siempre por letras o por el símbolo '_' barra baja

Las variables en python adquieren el 'tipo' de manera dinámica es decir según el valor que contengan.
por ejemplo: 
"""

num_int = 5  # Adquiere el tipo int (Integer) Entero, números sin decimales.
num_dec = 7.3  # Adquiere el tipo float Flotante, para números con decimales.
val_str = "Cualquier texto"  # Adquiere el tipo String Cadena, para carácteres alfanuméricos, letras, números, etc.

"""
Aunque la variable adquiere el tipo de manera automática según el valor inicial, si la intentamos reescribir
con otro valor de otro tipo, esta variable mantiene el tipo inicial, por ejemplo, una variable que se declaró 
al inicio con un valor Entero luego no podremos añadirle texto sin modificar explcitamente el tipo.

Aunque las variables tipo str contengan números no se puede operar con ellas como si lo fueran, en realidad son 
texto
"""

# Concatenar variables
"""
Para 'unir' variables podemos hacerlo de alguna de estas maneras, hay más pero aquí se muestran 3
"""

print("El valor es:", num_int)
"""
Al poner una coma realizamos la concatenación de dos variables de tipo distinto, además aade un espacio entre ambas
"""
print("El valor es: %i" % num_int)
"""
El símbolo '%' es un marcador que indica a python que debe incluir un valor, la letra 'i' indica a python 
el tipo de valor que debe incluir, en este caso un integer.
"""
print("El valor es: " + str(num_int))
"""
En este caso, se modifica el tipo de la varialbe 'num_int' de un integer a una string y se suma al texto 
"""

# Concatenar Variables tipo float

print("Concatenando decimales:", num_dec)
print("Concatenando decimales: %f" % num_dec)  # Por defecto concatena e incluye hasta seis decimales variables tipo float
print("Concatenando decimales: %.3f" % num_dec)  # Concatenamos y sólo representa tres decimales.
print("Concatenando decimales: " + str(num_dec))  # Concatenando combiertiendo el tipo de variable

# Concatenar Variables tipo string

print("Concatenando strings:", val_str)
print("Concatenando strings: %s" % val_str)
print("Concatenando strings: " + val_str)

# Introducción de datos
login = input("Login: ")
contrasenya = input("Contraseña: ")

print("El usuario logeado es: %s y la contraseña escrita es %s" % (login, contrasenya))

""" En este caso se han concatenado dos variables con el texto y al final del mismo hemos indicado como parametro y en 
orden el nombre de los mismos """

# Operaciones matemáticas simples

print(10 + 10)  # Suma
print(10 + (50 + 50))  # Suma con precedencia

print(10-10)  # Restas
print(1000-80)

print(10/5)  # División, siempre devuelve al menos un decimal, aunque este sea 0. El tipo de resultado es float
print(10/6)
print(10//6)  # Esta expresión realiza una división ignorando los decimales producidos, el tipo es int

print(10 * 800)  # Multiplicación
print(55 * 5)

# Obtención del resto de una división.

""" La obtención del resto de un división es útil para, por ejemplo, comprobar si un número es par o impar"""

print(3 % 2)  # Resto 1
print(4 % 2)  # Resto 0
print(5 % 2)
print(7 % 3.1)

# Pequeño programa para dividir dos números

num1 = float(input("Introduzca un número: "))

"""Primero solicitamos un número, input, por defecto, adquiere datos tipo string, por ello, hay que indicar 
el tipo dedato como número, en este caso tipo float
"""
num2 = float(input("Introduzca otro número: "))

print()  # este print sólo sirve para dejar un espacio en blanco entre la información mostrada.

division = num1 / num2
resto = num1 % num2

print(num1, "dividido entre", num2, "es igual a:", division) # Concatenamos los datos con su descripción...
print("El resto de", num1, "y", num2, "es igual a:", resto)


# Pencias y raíces

print(10**2)  # Para realizar la potencia de un número
print(100**0.5)  # Para realizar la raiz cuadrada
print(100**(1/2))  # Otra forma de hacer la riaz cuadrada
print(100**(1/3)) # Raiz cúbica ...

# Operadores de igualdad

a = True
b = False
print("Si 'a' es", a, "y 'b' es", b, "entonces ¿Son iguales?", a == b)
print("Si 'a' es", a, "y 'b' es", b, "entonces ¿Son diferentes?", a != b)

print("3 es mayor que 3", 3 > 3)
print("5 es menor que 5.1", 5 > 5.1)
print("5 es menor o igual que 5.1", 5 <= 5.1)
print("5 es menor o igual que 5.1", (5 < 5.1) or (5 == 5.1))  # Esta expresión es igual a la anterior pero desglosada

