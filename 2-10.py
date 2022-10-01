## Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de[0,100.000].

#carpetas
from random import randint;

#variables
random = int();
maximo = int();

random = 0;
maximo = 0;

#desarrollo

for i in range (10000):
    random = randint(0, 100000);
    if (random > maximo):
        maximo = random;

print("El numero mas grande de 10.000 numeros fue: ", maximo);

