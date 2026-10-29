password="admin"
intentos=3
acierto=False
while intentos>0:
    contra=input("Introduce contraseña ")
    if contra==password:
        print("Usuario válido!")
        acierto=True
        break
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
if not acierto:
    print("Usuario no válido!")

    