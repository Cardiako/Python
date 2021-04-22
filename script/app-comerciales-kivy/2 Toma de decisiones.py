"""
La toma de decisiones se lleva a cabo mediante condicionales, en este caso los condicionales son:
if -> Si la condición es True, verdadera, entonces realiza la acción.
elif -> Si no, comprueba si es verdadera con la siguiente condición y realiza la acción.
else -> Si ninguna de las anteriores se cumple, entonces realiza la siguiente acció
"""

"""
accion = int(input("Introduzca '1' para Sí y '2' para No: "))  # Introducimos un valor númerico entero
if accion == 1:  # Comparamos si el valor de la variable es igual a 1.
    print("Usted eligió Sí")  # De ser así, imprimimos el mensaje.
elif accion == 2:  # Si no se cumplió la primera condición comprueba la segunda.
    print("Usted elgió No")  # De ser así, imprimimos el mensaje.
else:  # Si ninguna de las condiciones anteriores se cumple
    print("Usted no elgió ni Sí ni No")  # entonces ejecuta esta acción.
"""

# Toma de decisiones mediante operadores
"""
Ahora vamos a usar operdadores para realizar comparaciones mediante los símbolos
'<'     Menor que
'>'     Mayor que
'<='    Menor o igual que
'>='    Mayor o igual que 
"""

edad = int(input("Introduzca su edad: "))
if edad <= 0:
    print("Su edad no puede ser igual o menor que '0'")
elif edad < 18:
    print("Su edad no puede ser inferior a '18' años")
elif edad >= 150:
    print("Su edad no puede ser igual o mayor a '150' años")
else:  # Con las anteriores condiciones ya se abarcan todas las edades inválidas, ahora solo se cumplen las válidas
    print("Su edad está entre 18 y 149 años")
