#Envío de paquetes
rtaUsuario = input("¿Desea envíar un paquete?\n Escriba 's' para si o 'n' para no:\n")
extras = []
rtasValidas = 0

if rtaUsuario == "n":
    print("Gracias por su tiempo, adios.")
elif rtaUsuario == "s":
    rtasValidas = rtasValidas + 1
    adds = input("¿Desea adquirir una estampilla o sobre?\n Escriba 1 para estampilla, 2 para sobre o 3 para ninguna o 4 para ambas\n")
    if adds == "1":
        extras.append("Estampilla")
        rtasValidas = rtasValidas + 1
    elif adds == "2":
        extras.append("Sobre")
        rtasValidas = rtasValidas + 1
    elif adds == "3":
        extras.append("Ninguna")
        rtasValidas = rtasValidas + 1
    elif adds == "4":
        extras.append("Estampilla y sobre")
        rtasValidas = rtasValidas + 1
    else:
        print("Ha elegido una opció incorrecta, abortando solicitud.")
else:
    print("Disculpe, no entiendo la respuesta, debe seleccionar 's' para si o 'n' para no.\nAbortando solicitud.")

#Imprimir respuesta al usuario
if rtasValidas == 2:
    print(f"Su paquete ha sido envíado.\nAñadidos seleccionados: {extras}\n Que tenga un buen día.")