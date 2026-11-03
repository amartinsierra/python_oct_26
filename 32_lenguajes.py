cursos="Java basico, Python principiantes, C, Java avanzado, Java enterprise, python web, cobol"

#solicitamos al usuario que introduzca un lenguaje y le mostramos
#todos los cursos relacionados con ese lenguaje
lista_cursos=cursos.split(",")
lenguaje=input("Que lenguaje te intereesa?")
for c in lista_cursos:
    if lenguaje.lower() in c.lower().split(" "):
        print(c)

