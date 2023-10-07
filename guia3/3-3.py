## Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
## a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
## b) Determinar la cantidad de números que son el cuadrado del número anterior
## c) Determinar la posición del mayor elemento impar de la secuencia

#variables
n = int();
n_anterior = int();
n_totales = int();
divisibles_x3 = int();
cuadrados_anterior = int();
i = int();
mayor = int();

n = 0;
n_anterior = 0;
n_totales = 0;
divisibles_x3 = 0;
cuadrados_anterior = 0;
i = 0;
mayor = -999999; #inicializo asi porque en ningun momento se especifica que no se puedan ingresar numeros negativos

#desarrollo
print("Ingresar la cantidad de numeros enteros deseada. Para terminar la carga ingrese un 0.");
n = int(input("Ingrese un numero: "));

while (n != 0):
    i += 1
    n_totales += 1;

    if (n % 3 == 0):
        divisibles_x3 += 1;

    if (n == n_anterior**2):
        cuadrados_anterior += 1;

    if (n%2 != 0):
        if (n > mayor):
            mayor = n;
            posición_mayor = i;

    n_anterior = n;
    n = int(input("Ingrese un numero: "));


# me falta el a)
print("Porcentaje de numeros divisibles por 3: %", divisibles_x3*100 / n_totales);
print("Cantidad de numeros que son el cuadrado del anterior:", cuadrados_anterior);
print("Posicion del mayor elemento IMPAR de la secuencia:", posición_mayor);

