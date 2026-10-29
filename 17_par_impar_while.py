#Se solicita la inserción de un número y el programa nos dirá
#si es par o impar. Después, se pregunta si quiere introducir otro número
#Si dice que sí(S), se vuelve a pedir el número y a indicar si es par o impar. 
#A continuación se vuelve a preguntar si quiere introducir otro número, y así hasta
#que diga que no(N)
resp="s"
while resp=="s" or resp=="S":
    num=int(input("Escribe un número "))
    if num%2==0:
        print("El número es par")
    else:
        print("El número es impar")
    resp=input("¿Desea introducir otro número(s/n)? ")