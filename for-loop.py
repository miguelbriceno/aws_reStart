print("Cuenta regresiva")
for x in range(0,11):
    print(x)

gameOn = True
while gameOn == True:
    num = input("Ingresa el número límite:\n")
    try:
        num = int(num)
    except:
        print("Debes ingresar un entero, prueba de nuevo.\n")
    else:
        print("La secuencia es:")
        for x in range(0,num+1):
            if x % 2 == 0:
                print(x)
        print("Gracias por jugar.\n")
        gameOn = False
        
gameOn2 = True
while gameOn2 == True:
    num = input("Ingresa el número límite:\n")
    try:
        num = int(num)
    except:
        print("Debes ingresar un entero, prueba de nuevo.\n")
    else:
        print("La secuencia es:")
        for x in range(0,num+1,2):
            print(x)
        print("Gracias por jugar.\n")
        gameOn2 = False