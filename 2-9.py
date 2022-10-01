## Promedio de números aleatorios: Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de[0,100000].


#carpetas
from random import randint;

#variables
random = int();
suma = int();
promedio = float();

random = 0;
suma = 0;
promedio = 0.0;

#desarrollo

for i in range (1000):
    random = randint(0, 100000);
    suma += random;

promedio = suma / 1000;

print("Promedio de 1000 numeros aleatorios: ", promedio);

