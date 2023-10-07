## Tito el robot: Desarrollar un programa controlado por menú de opciones, que permita simular el desplazamiento de un robot sobre un plano.
## Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y). Luego se presenta un menú de opciones que permita los siguientes movimientos:
## a) Girar al norte y avanzar 10 pasos
## b) Girar al sur y avanzar 20 pasos
## c) Girar al este y avanzar 10 pasos
## d) Girar al oeste y avanzar 20 pasos 
## El programa debe mostrar la ubicación del robot al inicio de cada



#carpetas 
from random import randint as ri;
from time import sleep;
#variables
x = int();
y = int();
opcion = str();

x = 0;
y = 0;
opcion = "";

#desarrollo 
x = ri(-200, 200);
y = ri(-200, 200);


while(True):
    print(" ")
    print("Posicion de TITO: (", x, ",", y, ")");
    sleep(1);

    print(""" 
a) Girar al norte y avanzar 10 pasos
b) Girar al sur y avanzar 20 pasos
c) Girar al este y avanzar 10 pasos
d) Girar al oeste y avanzar 20 pasos  """);

    opcion = str(input("Que quiere que haga TITO?: "));
    while (opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d"):
        opcion = str(input("Error. Eliga una opcion valida: "));
    opcion = opcion.lower();
    
    if (opcion == "a"):
        if (y <= 190):
            y += 10;
        else:
            print("TITO no se puede mover mas al Norte.");
    
    if (opcion == "b"):
        if (y >= -180):
            y -= 20;
        else:
            print("TITO no se puede mover  mas al Sur.");

    if (opcion == "c"):
        if (x <= 190): 
            x += 10;
        else:
            print("TITO no se puede mover mas al Este.");
        

    if (opcion == "d"):
        if (x >= -180):
            x -= 20;
        else:
            print("TITO no se puede mover mas al Oeste")

