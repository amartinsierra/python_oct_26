#lista de reproducción
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]

"""
def comprobar_cancion(titulo):   
    for can in lista_reproduccion:
        if can["titulo"]==titulo:
            return True
    return False  #si llega aquí es porque no ha encontrado el título
"""
def comprobar_cancion(titulo):
    return titulo in [can["titulo"] for can in lista_reproduccion]
    
#Se solicita la introducción de los datos de una nueva canción.
#si la canción no existe, se agrega a la lista. Si ya existe no se hace nada
#Después, el programa muestra todos los titulos almacenados
#y la valoración media de toda la lista de reproducción
titulo=input("Introduce el título de la canción:")
duracion=float(input("Introduce la duración de la canción:"))
valoracion=int(input("Introduce valoración de la canción:"))
cancion={"titulo":titulo,"duracion":duracion,"valoracion":valoracion}
if not comprobar_cancion(titulo):
    lista_reproduccion.append(cancion)
else:
    print("La canción no fue añadida")
suma=0
for c in lista_reproduccion:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"Valoración media {suma/len(lista_reproduccion)}")
