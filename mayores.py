print("¿Cual es mayor?")

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
except:
    print("Solo enteros por favor.")
else:
    if num1 > num2 and num1 > num3:
        print(f"El mayor es {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"El mayor es {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"El mayor es {num3}")
    else:
        print("No puedo determinar cual es mayor.")

        
