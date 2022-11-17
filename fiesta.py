print("Bienvenido a la fiesta\n")

try:
    edad = int(input("¿Que edad tienes?:\n"))
except:
    print("No es un entero, escriba la edad en enteros por favor.")
else:
    if edad <= 9:
        print("¡Pa la zona de juegos pelao!... O al restaurante con sus papás.")
    elif edad >= 18:
        print("Siga al bar distinguido señor, o a restaurante si lo desea.")
    else:
        print("Ta muy joven pa' beber y muy grande pa' jugar, siga al restaurante pues.")
finally:
    print("Gracias por venir.")