## Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:Determinar el menor de los numeros genera dos en forma aleatoria.Calcular el valor promedio de los números menores a 10.000.


#carpetas
from random import randint;

#variables
n = int();
menor = int();
suma_menores10mil = int();
i_menores10mil = int();

bandera = bool();

n = 0;
menor = 0;
suma_menores10mil = 0;
i_menores10mil = 0;

bandera = True;

#desarrollo

for i in range (5000):
    n = randint(0, 100000);
    
    if (bandera == True):
        menor = n;
        bandera = False;

    if (n < menor):
        menor = n;

    if (n < 10000):
        suma_menores10mil += n;
        i_menores10mil += 1;



print("De 5000 numeros, el menor fue: ", menor);
print("Valor promedio de los numeros menores a 10.000: ", suma_menores10mil/i_menores10mil);


