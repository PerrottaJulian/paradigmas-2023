## Menu de Opciones con secuencias. Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones: 
## a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados 
## b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
## c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
## d) Salir


#carpetas
import time;


#variables
opcion = str();
n_a = int();
suma_cuadrados = int();
texto = str();
espacio = int();
palabra = str();
terminan_vocal = int();
n_c = int();
pares = int();
impares = int();


opcion = "";
n_a = 0;
suma_cuadrados = 0;
texto = "";
espacio = 0;
palabra = "";
terminan_vocal = 0;
n_c = 0;
pares = 0;
impares = 0;

#desarrollo

input("Presione Enter para ingresar");

print("Ingresando", end="...");
time.sleep(1);
print("...", end="");
time.sleep(1);
print("...", end="");
time.sleep(0.8);

while(True):

    print(""" 
    ***************** MENU OPCIONES ***********************
    ** a) Suma de los cuadrados                          ** 
    ** b) Cantidad de palabras que finalizan con vocales **
    ** c) Mayor cantidad de pares o impares              **
    ** d) Salir                                          **    """);

    opcion = str(input("Que opcion elige?: "));
    opcion = opcion.lower();

    while (opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d"):
        opcion = str(input("Hubo un error, eliga una opcion valida: "));


    time.sleep(1);
    # a)
    if (opcion == "a"):
        #explicado en la opcion c
        suma_cuadrados = 0;
        #

        print("Debera ingresar una serie de numeros enteros mayores a 0, la carga finaliza cuando se ingresa 0 y se mostrara la suma de los cuadrados de los numeros ingresados");

        n_a = int(input("Ingrese un numero: "));
        while (n_a < 0):
            n_a = int(input("Error. Ingrese un numero valido: "));

        while (n_a != 0):
            suma_cuadrados += n_a ** 2;

            n_a = int(input("Ingrese un numero: "));
            while (n_a < 0):
                n_a = int(input("Error. Ingrese un numero valido: "));

        print("Resultado:", suma_cuadrados);

        time.sleep(1);
        print("Volviendo al menu", end="...");
        time.sleep(1);
        print("...", end="");
        time.sleep(1);
        print("...", end="");
        time.sleep(0.8);

    # b)
    if (opcion == "b"):
        #
        terminan_vocal = 0;
        #

        print("Debera ingresar un texto, que debe finalizar con un punto, y se determinara la cantidad de palabras que terminan con una vocal");
        texto = str(input("Texto: "));

        while (texto[len(texto) - 1] != "."):
            print("OJO! El tecto debe terminar con un punto");
            texto = str(input("Pruebe devuelta: "));
        
        for i in range (len(texto)):
            espacio = texto.find(" ");
            palabra = texto[0 : espacio];

            texto = texto[espacio+1 : texto.find(".")+1];

            if (palabra[len(palabra)-1] == "a" or palabra[len(palabra)-1] == "e" or palabra[len(palabra)-1] == "i" or palabra[len(palabra)-1] == "o" or palabra[len(palabra)-1] == "u"):
                terminan_vocal += 1;

        print("Cantidad de palabras que terminan en vocal:", terminan_vocal);
        
        time.sleep(1);
        print("Volviendo al menu", end="...");
        time.sleep(1);
        print("...", end="");
        time.sleep(1);
        print("...", end="");
        time.sleep(0.8);

    # c)
    if (opcion == "c"):
        #si volves a elegir la opcion c una segunda vez, los valores que las variables tenian se mantiene y se suman a lo nuevo que ingrese, dando resultados erroneos
        pares = 0;
        impares = 0;
        #

        print("Debera ingresar una serie de numeros enteros y se determinara si hay mayor cantidad de pares o de impares. Para terminar la carga ingresar 0");
        n_c = int(input("Ingresar un numero: "));

        while (n_c != 0):
            if (n_c % 2 == 0):
                pares += 1;
            else:
                impares += 1;
            
            n_c = int(input("Ingresar un numero: ")); 
        
        if (pares > impares):
            print("Hay mas PARES que impares");
        elif (pares < impares):
            print("Hay mas IMPARES que pares");
        else:
            print("Hay la mimsma cantidad de PARES e IMPARES")

        time.sleep(1);
        print("Volviendo al menu", end="...");
        time.sleep(1);
        print("...", end="");
        time.sleep(1);
        print("...", end="");
        time.sleep(0.8);

    # d)
    if (opcion == "d"):
        time.sleep(0.5);
        print("Saliendo", end="...");
        time.sleep(1);
        print("...", end="");
        time.sleep(1);
        print("...",);
        time.sleep(1);
        print("Hasta luego!");
        time.sleep(0.5);
        break


