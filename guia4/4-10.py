## Diseñar el algoritmo correspondiente a un programa, que:
## a) Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
## b) Carga la tabla con valores numéricos enteros.
## c) Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

#carpetas
from random import randint

#variable


#
tabla = [];
for i in range (5):
  fila = [];
  
  for i in range (5):
    r = randint(1,100);
    fila.append(r);

  tabla.append(fila);

for fila in tabla:
  print(fila);

for fila in (tabla): #suma filas
  suma_fila = 0;
  for n in (fila):
    suma_fila += n;
    
  print("Suma de la fila", tabla.index(fila) + 1, "=", (suma_fila));  

for elemento in range(len(tabla)): #suma columnas
  suma_columna = 0;
  for fila in tabla:
    
    suma_columna += tabla[tabla.index(fila)][elemento];
    
  print("Suma de la columna", elemento + 1, "=", suma_columna);
  
