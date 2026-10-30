cursos=["Java","Python","Typescript","C","Dart"]
#Pregunta al usuario que lenguaje quiere aprender, y el programa
#le indicará si existe un curso para ese lenguaje o no
lenguaje=input("¿Qué lenguaje quieres aprender?")

"""
encontrado=False
for c in cursos:
    if c.lower()==lenguaje.lower():
        print("Tengo ese curso!")
        encontrado=True
        break
if not encontrado:
    print("Lo siento, no tengo ese curso")
"""
if lenguaje.lower() in [c.lower() for c in cursos]:
   print("Tengo ese curso!")
else:
   print("Lo siento, no tengo ese curso") 