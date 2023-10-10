lista = [1,2,5,4]
todo_numeros = True

for n in lista:
    if str(n).isdigit() is False:
        todo_numeros = False

print(todo_numeros)

if not todo_numeros:
    print("No hay solo numeros")
else:
    print("Hay solo numeros")