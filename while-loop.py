# Importaciones
import random

# Definción de variables
numeroEscondido  = 0
numeroUsuario = 0
usuarioGana = False
intentos = 1
opcionesValidas = ["1","2","3","4","5","6","7","8","9","10"]

# Inicia el juego
print("Vamos a jugar un juego.\nVoy a pensar en un número del 1 al 10, y tendrás tres intentos para adivinarlo, ¿ok?\n¡Vamos a darle! El número es...\nLo tengo, tu turno:\n")
# Inicia el cilco
numeroEscondido = random.randint(1,10)
while usuarioGana != True and intentos <= 3:
    numeroUsuario = input(f"Intento {intentos}: ")
    # Validar si el número ingresado está dentro de las opciones dsiponibles
    validacion = numeroUsuario in opcionesValidas
    if validacion != True:
        print(f"{numeroUsuario} no es un número entero entre 1 y 10, prueba escibiendolo de nuevo.")
    else:
        numeroUsuario = int(numeroUsuario)
        # Validar si los números coinciden
        if numeroUsuario == numeroEscondido:
            usuarioGana = True
            print(f"¡Ganaste! {numeroUsuario} era el número correcto.")
        else:
            print("Ese no es, ¡voy a ganar!")
            intentos += 1
# Mensaje de derrota
if intentos >= 3 and usuarioGana != True:
    print(f"\n¡Yo gané!\nEl número correcto era {numeroEscondido}.\nMejor suerte la próxima.")
    
