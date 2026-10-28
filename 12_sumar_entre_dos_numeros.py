#Solicita la introducción de dos números y calcula suma de todos los números
#comprendidos entre el menor y el mayor
num1=int(input("Primer número "))
num2=int(input("Segundo número "))
suma=0
#solución 1
if num1<num2:
    menor,mayor=num1,num2
else:
    menor=num2
    mayor=num1
    
for n in range(menor,mayor+1):
    suma=suma+n

#solución 2
"""
if num1<num2:
    for n in range(num1,num2+1):
        suma=suma+n
else:
    for n in range(num2,num1+1):
        suma=suma+n

#solución 3
if num1>num2:
    num1,num2=num2,num1
    
for n in range(num1,num2+1):
    suma=suma+n
"""
print("La suma es ",suma)