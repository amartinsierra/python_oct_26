#lee la nota de un alumno y dependiendo del número (0 -10)
#le indica si es suspenso (menos de 5), aprobado (5 o 6),
#notable (7 o 8) o sobresaliente (9 o 10)
#utilizamos match
nota=int(input("Introduce nota: "))
match nota:
    case 0|1|2|3|4:
        print("Estás suspenso")
    case 5|6:
        print("Estás aprobado")
    case 7|8:
        print("Tienes un notable")
    case 9|10:
        print("Tienes un sobresaliente")
    case _:
        print("Nota no válida")