## Menú de opciones y validación Se pide desarrollar un programa controlado por menú de opciones que permita lo siguiente:
## 1. Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio.
## 2. Generar n valores aleatorios entre -100 y 100 (n se ingresa por teclado). Determinar la cantidad de valores negativos y positivos.
## 3. Cargar la nota de un alumno e informar si está aprobado teniendo en cuenta que la nota es un valor entre 0 y 10, siendo mayor o igual a 4 si está aprobado


#carpetas
from time import sleep;
from random import randint as ri;

#variables
opcion = int();
n1 = int();
n2 = int();
random = int();
nota = int();

opcion = "";
n1 = 0;
n2 = 0;
random = 0;
nota = 0;

#desarrollo
input("Presione Enter para ingresar");

print("Ingresando", end="...");
sleep(1);
print("...", end="");
sleep(1);
print("...", end="");
sleep(0.8);


while(True):

    print(""" 
    ***************** MENU OPCIONES ***********************
    ** 1- Promedio de numeros                                   ** 
    ** 2- Numeros aleatorios: Cantidad de negativos y positivos **
    ** 3- Nota de alumno                                        **
    ** 4- Salir                                                 **    """);

    opcion = int(input("Que opcion elige?: "));
    while (opcion < 1 or opcion > 4):
        opcion = int(input("Hubo un error, eliga una opcion valida: "));


    sleep(1);
    if (opcion == 1):
        suma_n1 = int();
        i1 = int();
        suma_n1 = 0;
        i1 = 0;

        print("Ingresar serie de numeros enteros positivos. La carga finaliza al ingresar -1. Se calculara el promedio.");

        n1 = int(input("Ingresar un numero: "));
        while (n1 != -1):
            suma_n1 += n1;
            i1 += 1;
            n1 = int(input("Ingresar un numero: "));
        
        print("Promedio =", suma_n1/i1);


    if (opcion == 2):
        i2 = int();
        negativos = int();
        positivos = int();
        i2 = 0;
        negativos = 0;
        positivos = 0;

        print("Se generaran una serie de numeros aleatorios entre -100 y 100. Usted determinara cuantos numeros. Se determinanra la cantidad de valores negativos y positivos");

        n2 = int(input("Cuantos numeros generar?: "));

        for i2 in range (n2):
            random = ri(-100, 100);
            if (random < 0):
                negativos += 1;

            elif (random > 0):
                positivos +=1;
        
        print("Numeros positivos:", positivos);
        print("Numeros negativos:", negativos);


    if (opcion == 3):

        print("Ingresar nota del alumno (entre 0 y 10) y se dira si esta aprobado o desaprobado.");

        nota = int(input("Ingresar nota: "));

        while (nota < 0 or nota > 10):
            nota = int(input("INGRESE UNA NOTA VALIDA: "));

        if (nota >= 4):
            print("El examen esta APROBADO.");
        else:
            print("El examen esta REPROBADO.");

       
    if (opcion == 4):
        sleep(0.5);
        print("Saliendo", end="...");
        sleep(1);
        print("...", end="");
        sleep(1);
        print("...",);
        sleep(1);
        print("Hasta luego!");
        sleep(0.5);
        break


