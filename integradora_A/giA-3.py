## Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). 
## Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.


def sucesión():
    nums = []
    n = 0
    while n != -1:
        try:
            n = int(input("Ingrese un numero: "));
            if n < -1:
                print("Solo puede ingresar numeros naturales (-1 para finalizar)")
        except:
            print("Solo puede ingresar numeros naturales")
            continue

        if n >= 0:
            nums.append(n)

    print(f"Numeros ingresados: {len(nums)}   Suma = {sum(nums)}  Promedio = {sum(nums)/len(nums)} ")

print("Debe ingresar una sucecion de numeros NATURALES. Para finalizar ingrese -1")
sucesión()