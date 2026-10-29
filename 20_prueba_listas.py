lista=[4,1,8,2,11]
print(lista)
#muestra los números pares de la lista
for num in lista:
    if num%2==0:
        print(num)
#sutituye cada elemento de la lista por su cuadrado
#y luego imprimes la lista entera y la suma de todo
#su contenido
"""
indice=0
for num in lista:
    lista[indice]=num**2
    indice=indice+1
"""
#solución alternativa a lo anterior
for indice,num in enumerate(lista):
    lista[indice]=num**2
print(lista)
suma=0
for num in lista:
   suma=suma+num
print(f"La suma de los datos de la lista {lista} es {suma}") 
    