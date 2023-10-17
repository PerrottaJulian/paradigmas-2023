"""
Ejercicio 2 para practicar listas, tuplas y diccionarios
Un mismo problema, 4 formas diferentes de resolverlo. ¿Se te ocurre alguna otra? 
“Dado un arreglo no vacío de números enteros, cada elemento aparece dos veces, excepto uno. 
Se debe encontrar el elemento que no se repite.”
"""

lista = [1,1,2,2,3,4,4]

for elemento in lista:
    if lista.count(elemento) == 1:
        print(f"El numero que no se repite en la lista es: {elemento}")