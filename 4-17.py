"""
Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados.
Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
"""
import time

n = 0
lista = []
print("Ingrese numeros positivos a la lista. Para detener el ingreso, colocar un numero negativo.")
while n >= 0: #Creo la lista primera
    try:
        n = int(input("Numero: "))
        if n>0:
            lista.append(n)
    except:
        print("Coloque un numero correcto (No se permiten numeros con coma)")
        continue
print(lista)

nueva_lista = []
for elemento in lista:
    
    if elemento not in nueva_lista: #Tambien: if nueva_lista.count(elemento) == 0
        nueva_lista.append(elemento)

print(nueva_lista)