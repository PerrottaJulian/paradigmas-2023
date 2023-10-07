## Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la tarjeta de bingo de una persona.
## Una vez generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, a parƟr de allí mostrar los siguientes mensajes:
## Si el usuario no marcó ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”.

#carpetas
from random import randint as r;

#variables
n_aleatorio = int();
num1 = int();
num2 =int();
num3 =int();

n_aleatorio = 0;
num1 = 0;
num2 = 0;
num3 = 0;

#desarrollo
tar_bingo = [];
for i in range (15):    
    n_aleatorio = r(0,100);
    tar_bingo.append(n_aleatorio);


print(tar_bingo)

print("Pruebe su suerte! Ingrese 3 numeros entre 0 y 100 y vea si alguno coincide con los de su tarjeta bingo.");
num1 = int(input("Numero 1: "));
num2 = int(input("Numero 2: "));
num3 = int(input("Numero 3: "));

i = 0
for i in range (15):
    if (num1 == tar_bingo[0 + i]):
        print("El jugador marcó algún número de la tarjeta (", num1, ")");
        quit();

    elif (num2 == tar_bingo[0 + i]):
        print("El jugador marcó algún número de la tarjeta (", num2, ")");
        quit();
    
    elif (num3 == tar_bingo[0 + i]):
        print("El jugador marcó algún número de la tarjeta (", num3, ")");
        quit();

print("El jugador tiene mala suerte, no marcó ninguna casilla")