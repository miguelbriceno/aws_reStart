import re

# Abrir archivo inicial
with open("preproinsulin-seq.txt", "rt") as lectura:
    cadena = lectura.read()

# Limpiar la cadena
cadena = re.sub("[A-Z0-9\s\/]", "", cadena)
preproInsulin = cadena

# Separar las proteinas
linsulin = cadena[0:24]
binsulin = cadena[24:54]
cinsulin = cadena[54:89]
ainsulin = cadena[89:110]
'''
#Guardar en archivos las cadenas
with open("linsulin-seq2.txt", "wt") as linsulinFile:
        linsulinFile.write(linsulin)
        
with open("binsulin-seq2.txt", "wt") as binsulinFile:
    binsulinFile.write(binsulin)

with open("cinsulin-seq2.txt", "wt") as cinsulinFile:
    cinsulinFile.write(cinsulin)

with open("ainsulin-seq2.txt", "wt") as ainsulinFile:
    ainsulinFile.write(ainsulin)
'''
# Generar insulina
insulin = binsulin + ainsulin

# Imprimir datos
print(f"La preproinsulina humana es: {preproInsulin}")
print(f"La insulina huma es, en su cadena a: {ainsulin}")

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Cuenta cuantas veces esta cada letra de aminiacido en la cadena insuin
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}) 
#print(aaCountInsulin) # Para pruebas
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("El peso molecular aproximado de la insulina: " +
str(molecularWeightInsulin))

# Obtener peso molecular
molecularWeightInsulinActual = 5807.63
print("Porcentaje de error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

pKR = {
    "y":10.07,
    "c":8.18,
    "k":10.53,
    "h":6.00,
    "r":12.48,
    "d":3.65,
    "e":4.25
}

# Conteo de aminoacidos que contrinuyen a la carga neta
#seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

seqCount = {}
for x in ['y','c','k','h','r','d','e']:
    conteo = float(insulin.count(x))
    seqCount[x] = conteo
#print(seqCount) # Para pruebas

pH = 0
while pH <= 14:
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), round(netCharge,2))
    pH += 1