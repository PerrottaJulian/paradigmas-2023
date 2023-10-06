## Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.


#carpetas
from random import randint;

#variables
numeros = [];

r = int();
temp = int();

r = 0;
temp = 0;

#desarrollo
for i in range(10):
    r = randint(0, 100);
    numeros.append(r);

print(numeros);

for i2 in range(len(numeros)): 

    for i3 in range(len(numeros)-1):
        if (numeros[i3] > numeros[i3+1]):
            temp = numeros[i3+1];
            numeros[i3+1] = numeros[i3];
            numeros[i3] = temp;

print(numeros);








