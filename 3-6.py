## Secuencia de n números. Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar: 
## a) Cuántos números ingresados terminan en 5 
## b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia 
## c) Cuántos números ingresados son mayores al anterior.

#carpetas
import time;

#variables
n_numeros = int();
num = int();
termina_en5 = int();
primer_num = int();
veces_primer_num = int();
num_anterior = int();
mayores_anterior = int();

bandera = bool();

n_numeros = 0;
num = 0;
termina_en5 = 0;
primer_num = 0;
veces_primer_num = 0;
num_anterior = 999999; #Inicializo asi para que el primer numero de la secuencia no cuente como mayor al anterior
mayores_anterior = 0;

bandera = True;

#desarrollo

print("Debera ingresar una secuencia de numeros enteros, cuya longitud la determinara usted. Se devolveran distintos datos de la secuencia.")
n_numeros = int(input("Longitud de la secuencia (tiene que ser mayor a 0): "));

while (n_numeros <= 0):
    n_numeros = int(input("ERROR. La longitud de la secuencia tiene que ser mayor a 0. Intente devuelta: "));


time.sleep(2);

for i in range (n_numeros):
    num = int(input("Ingrese un numero: "));
    if (bandera == True):
        primer_num = num;
        bandera = False;
    
    if (num % 5 == 0 and num % 10 != 0):
        termina_en5 += 1;

    if (num == primer_num):
        veces_primer_num += 1;

    if (num > num_anterior):
        mayores_anterior += 1 

    num_anterior = num;

print("Numeros que terminan en 5:", termina_en5); #a
print("Cantidad de veces que aparece el primer número ingresado:", veces_primer_num); #b
print("Numeros mayores al anterior:", mayores_anterior); #c