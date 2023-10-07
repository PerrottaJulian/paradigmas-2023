"""
Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
Entonces se debe imprimir el vector (sólo los elementos introducidos).
"""

lista = []
n = 0
while n > -1:
    try:
        n = int(input("Ingresar numero: "))
    except:
        print("Error, no ingreso un numero")
        continue
    if n > -1:
        lista.append(n)

print(f"Vector: {lista}")