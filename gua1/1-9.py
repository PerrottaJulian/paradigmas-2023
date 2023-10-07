#Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

#variables
n = int();
tabla = int();

n = 0;
tabla = 0;
#desarrollo
n = int(input("Ingresar un numero. Se mostrara su respectiva tabla del 1 al 10: "));


for c in range(1,10+1):
    tabla = n * c;
    print(tabla);












