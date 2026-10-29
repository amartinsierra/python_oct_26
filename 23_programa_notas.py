#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir

notas=[]
opcion_elegida=0
while opcion_elegida!=6 :
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            notas.append(int(input("Introduce nota ")))
        case 2:
            print(f"nota más alta {max(notas)}")
            print(f"nota más baja {min(notas)}")
        case 3:
            aprobados=0
            for nota in notas:
                if nota>=5:
                    aprobados+=1
            print(f"total de aprobados {aprobados}")
        case 4:
            suma=0
            for nota in notas:
                suma+=nota
            if(len(notas)==0):
                print("No hay notas")
            else:
                print(f"nota media {suma/len(notas)}")
        case 5:
            print(notas)
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida")
    
