numeros=[3,-1,-9,4,2,11,-8,7,-5]
#crea una lista a partir de la anterior que contenga
#solo los positivos
positivos=[]
"""
for n in numeros:
    if n>=0:
        positivos.append(n)
"""
positivos=[n**2 for n in numeros if n>=0]        
print(positivos)

#indica si hay algún número par en la lista

if [n for n in numeros if n%2==0]:
    print("hay algún par")
else:
    print("no hay par")