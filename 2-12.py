## Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. Los requerimientos funcionales del programa son:
## La sumatoria de solo los números que estén comprendidos entre 50 y 100. Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. Informar si en la carga de números se ingreso al menos un número 0. Informar si la serie contiene solo números pares e impares alternados.


#variables 
n = int();
suma_entre50y100 = int();
n_pares = int();
n_impares = int();
tiene_0 = bool();

n = 0;
suma_entre50y100 = 0;
n_pares = 0;
n_impares = 0;
tiene_0 = False;

#desarrollo
n = int(input("Ingresar los numeros enteros que desee. Para terminar la carga de numeros, ingrese un numero negativo: "));

while (n >= 0):

    if (n >= 50 and n <= 100):
        suma_entre50y100 += n;


    if (n%2 == 0 and n>0):
        n_pares += 1;
    elif (n%2 != 0 and n>0):
        n_impares += 1;


    if (n == 0):
        tiene_0 = True;

    n = int(input(""));


print("La sumatoria de los numeros comprendidos entre 50 y 100 es:", suma_entre50y100);
print("Cantidad de numeros pares ingresados:", n_pares);
print("Cantidad de numeros impares ingresados:", n_impares);

if (tiene_0 == True):
    print("Se ingreso al menos un 0");
else:
    print("No se ingreso un 0");