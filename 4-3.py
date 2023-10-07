"""
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
"""
notas = []


for i in range(5):
    nota = int(input(f"Ingrese la nota del {i+1} examen: "))
    while nota < 0 or nota > 10:
        nota = int(input(f"Error. Vuelva a ingresar la nota del {i+1} examen: "))
    notas.append(nota)


print("Notas: ", end="")
for nota in notas:
    print(f"{nota}, ", end="")
print("\n")

print(f"Nota mas alta: {max(notas)}")
print(f"Nota mas baja: {min(notas)}")
print(f"Promedio: {sum(notas)/len(notas)}")

