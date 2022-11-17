
# Generar listas comprimidas
lista = [x for x in range(0,13) if x % 2 == 0]
print(f"Lista: {lista}")

multiplosTres = [x for x in lista if x % 3 == 0]
print(f"Multiplo 3: {multiplosTres}")

repetidos = [x for x in multiplosTres for y in lista if x == y]
print(f"Repetidos: {repetidos}")

# Trabajo con cadenas
cadena = "Hola pinche mundo cruel. Adenás que tamvien les digo que yayo es mi hermano."
diccionario = ["A", "E", "I", "O", "U"]
extraccion = {}

cadena = cadena.upper()

for x in diccionario:
	for y in cadena:
		conteo = cadena.count(x)
		extraccion[x] = conteo
print(f"Extraccion:  {extraccion}")

# "x:" represneta la llave, que es el iterador de diccionario.
# De los ":" en adelante son las operaciones que se realizan para obtener el valor correspondiente.
extraccion2 = {x: (cadena.count(x)) for x in diccionario for y in cadena}
print(f"Extraccion2: {extraccion2}")

seqCount = ({x: float(cadena.count(x)) for x in ['Y','C','K','H','R','D','E']})
print(f"seq:  {seqCount}") # Para pruebas

seqCount2 = {}
for x in ['Y','C','K','H','R','D','E']:
    conteo = float(cadena.count(x))
    seqCount2[x] = conteo
print(f"seq2: {seqCount2}") # Para pruebas

# Recorrer diccionario
# Se definen variables para llave y valor y se usa el metodo items().
for key, val in seqCount.items():
	val += 1.1
	print(f"Llave: {key} - Valor: {val}")

# Crear un nuevo diccionario con un for basado en dos listas
newDicc = {}
for x in multiplosTres:
	for y in diccionario:
		if y != "U":
			newDicc[x] = y
print(f"newDic:  {newDicc}") # Para pruebas

# Comprension de listas para diccionarios
# Se empieza definiendo los valores que se desean colocal como llaves y valores
# Luego con el ciclo interior y luego el exterior
# Y por último la condicion si l hay
newDicc2 = {x:y for y in diccionario for x in multiplosTres if y != "U"}
print(f"newdic2: {newDicc2}") #Para pruebas

# Crear diccionario a partir de un diccionario y una lista
ultraDic = {}
for x,y in newDicc.items():
	for i in diccionario:
		ultraDic[x] = i
print(f"ultradic:  {ultraDic}") #Para pruebas


ultraDic2 = {x:i for i in diccionario for x,y in newDicc.items()}
print(f"Ultradic2: {ultraDic2}") # Para pruebas


# Crear diccionario a partir de un diccionario y una lista
superDic = {}
for x in diccionario:
	for y,z in newDicc.items():
		superDic[y] = x+z
print(f"Superdic:  {superDic}") #Para pruebas

superDic2 = {y:(x+z) for y,z in newDicc2.items()}
print(f"Superdic2: {superDic2}") # Para pruebas




'''
La comprension de listas es una forma abreviada de hacer ciclos for.
Se deben leer del centro hacia la derecha y por último la izquierda.
En el centro irá el ciclo for padre, y a la derecha el hijo.
Cuando hay condiciones van a la derecha del cliclo.
Pero cuando hay operaciones con el iterador del ciclo padre, estás van a la izquierda.
La variable donde se guarda la expresion define el tipo de dato que se obtiene.

SINTAXIS
<new_list> = [<expression> for <item> in <iterable>]
'''

