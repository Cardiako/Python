"""
1) Realice un algoritmo que imprima solamente su nombre en la pantalla y seguidamente finalice la aplicación.
"""
#print("Abel")

"""
2) Realice un algoritmo que solicite al usuario que escriba su nombre y seguidamente envíe la siguiente frase a la 
salida estándar: "Su nombre es: [nombre del usuario]".
"""
#nombre = input("Por favor, escriba su nombre: ")
#print("Su nombre es:", nombre)

"""
3) Realice un algoritmo que solicite el nombre y la edad del usuario., seguidamente, envíe la siguiente frase a 
la consola: "El nombre es <nombre> y su edad es <edad>"
"""
#nombre = input("Por favor, escriba su nombre: ")
#edad = input("¿Cual es su edad: ?")
#print("El nombre es %s y su edad es %s" % (nombre, edad))

"""
4) Realice un algoritmo que solicite al usuario informar un número. Seguidamente, almacene a este número en una 
variable. Por último, envíe a ese número a la salida estándar.
"""

#numero = int(input("Por favor, introduzca un número "))
#print(numero)

"""
Realice un algoritmo que solicite al usuario informar un número. Seguidamente, escriba el siguiente mensaje  
"El número escrito fue:   "
"""

#numero = int(input("Por favor, introduzca un número "))
#print("El número escrito fue:" ,numero)

"""
6) Realice un algoritmo que solicite al usuario informar 3 números. Seguidamente, sume los valores y envíe a la 
salida estándar la siguiente frase "La suma total es:  ".
"""

#numero1 = int(input("Por favor, introduzca el primer número "))
#numero2 = int(input("Por favor, introduzca el segundo número "))
#numero3 = int(input("Por favor, introduzca el tercer número "))
#print("La suma total es:", numero1 + numero2 + numero3)

"""
7) Realice un algoritmo que solicite al usuario informar 2 números. Seguidamente, sume los valores y envíe a la 
salida estándar la siguiente frase: "La suma entre <X> e <Y> es igual a <total>"
"""

#numero1 = int(input("Por favor, introduzca el primer número "))
#numero2 = int(input("Por favor, introduzca el segundo número "))
#print("La suma entre %i y %i es igual a %i " % (numero1, numero2, numero1 + numero2))

"""
8) Realice un algoritmo que solicite las notas de las 4 pruebas semestrales al usuario. Seguidamente, calcule la 
media y envíe el valor resultante a la salida estándar:
"""
"""
nota1 = float(input("Por favor introduzca la primera nota: "))
nota2 = float(input("Por favor introduzca la segunda nota: "))
nota3 = float(input("Por favor introduzca la tercera nota: "))
nota4 = float(input("Por favor introduzca la cuarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("La media de las siguentes cuatro notas, %.2f, %.2f, %.2f, %.2f, es: %.3f " % (nota1, nota2, nota3, nota4, media))
"""

"""
9) Realice un algoritmo que solicite al usuario que informe una medida en metros. Seguidamente, convierta a esta 
medida de metros a centímetros y envíela a la salida estándar.
"""
"""
metros = float(input("Por favor introduzca su medida en metros: "))
centimetros = metros * 100

print("Su medida en centimetros es:", centimetros)
"""

"""
10) Realice un algoritmo que calcule el cubo y el cuadrado de un determinado número:
"""
"""
numero = float(input("Por favorintroduzca un número: "))
cuadrado = numero ** 2
cubo = numero ** 3

print("El cuadro y el cubo de %.1f son %.1f y %.1f" % (numero, cuadrado, cubo))
"""

"""
11) Realice un algoritmo que solicite al usuario que escriba 2 números. Seguidamente, imprima el total de la 
división en números  decimales y el total de la división en números enteros ( es decir, sin casillas decimales).
"""
"""
dividendo = float(input("Por favor introduzca el dividendo "))
divisor = float(input("Por favor introduzca el divisor "))
division = dividendo / divisor

print("La dividision con decimales es: %.3f y la división entera es: %.0f" % (division, division))
"""

"""
12) Realice un algoritmo que solicite al usuario la longitud y la altura de un cuadrado. Seguidamente, imprima
para el usuario cuántos metros cuadrados posee el área total del cuadrado.
"""
"""
longitud1 = float(input("Por favor introduzca la primera medida del cuadrado: "))
longitud2 = float(input("ahora, la segundamedida:"))
area = longitud1 * longitud2

print("El área del cuadrado es: %.3f" % area)
"""

"""
13) Realice un algoritmo que solicite al usuario informar una cantidad de días, horas, minutos y segundos. 
Seguidamente, convierta todo a segundos.
"""

"""
dias = int(input("Introduzca el número de días: "))
horas = int(input("Introduzca el número de horas: "))
minutos = int(input("Introduzca el número de minutos: "))
segundos = int(input("Introduzca el número de segudos: "))
convSeg = (((dias * 24 + horas) * 60) + minutos) * 60 + segundos

print("El tiempo en segudos es:", convSeg)
"""

"""
14) Realice un algoritmo que solicite al usuario informar el valor de una compra.Seguidamente, aplique un 10% 
de descuento e imprima en la pantalla tanto el valor total como el valor con el descuento aplicado.  
"""

precio = float(input("¿Cuanto le acostado la compra? "))
descuento = precio * 0.9
descApli = precio * 0.1
print("El precio sin descuento es de %.2f y con descuento es de %.2f  El precio descontado asciende a %.2f"
      % (precio, descuento, descApli))
1