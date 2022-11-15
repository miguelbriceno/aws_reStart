miCadena = "Esta es una cadena."
print(miCadena)

print(miCadena)
print(type(miCadena))
print(str(miCadena) + " es del tipo de dato " + str(type(miCadena)))

primeraCadena = "Caida de"
segundaCadena = " agua."
tercerCadena = primeraCadena + segundaCadena
print(tercerCadena)

nombre = input("¿Como se llama su merced?\n")
print("Hola " + nombre)

color = input("¿Cúal es su color favorito " + nombre + "?\n")
animal = input("¿Cúal es su animal favorito " + nombre + "?\n")
print("A {} le gusta un {} de color {}.".format(nombre,animal,color))
print(f"A {nombre} le gusta un {animal} de color {color}.")