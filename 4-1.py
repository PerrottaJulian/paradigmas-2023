## Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

#carpetas 
import random

#variables 
nums = [];

#desarrollo
for i in range (10):
    r = random.randint(1, 10)
    nums.append(r)

for num in nums:
    print(f"{num}, {num**2}, {num**3}")







