# Establecer variables
cadena = "Hola compas esta es una prueba"
llaves = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
diccConteo = {}
diccValores = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 
valorTotal = 0

# Pasar cadena a mayusculas
cadena = cadena.upper()
#print(cadena) # Para verificación

# Recorrer y contar cuantas veces está cada letra en la cadena
for x in llaves:
    conteo = cadena.count(x)
    diccConteo[x] = float(conteo)
#print(diccConteo) # Para verificación

# Multiplicar las cantidades por los valores
for x in diccConteo:
    valorTotal += diccConteo[x]*diccValores[x]
print(f"El valor total es: {valorTotal}")