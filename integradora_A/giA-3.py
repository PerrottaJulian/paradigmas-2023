## Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). 
## Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.


def sucesión():
    c = 0;
    sum = 0;
    n = int(input("Ingrese un numero: "));
    while n != -1:
        if n >= 0:
            c +=1;
            sum += n;
        n = int(input("Ingrese un numero: "));
    print(f"Numeros ingresados: {c}   Suma = {sum}  Promedio = {sum/c} ")

print("Debe ingresar una sucecion de nuemeros NATURALES. Para finalizar ingrese -1")
sucesión()