## Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

#carpetas 
from random import randint as ri;

#variables 
nums = [];

random = int();
random = 0;

#desarrollo
for i in range (10):
    random = ri(1, 10);
    nums.append(random);

for i2 in range (10):
    print(nums[i2], ",", nums[i2]**2, ",", nums[i2]**3);







