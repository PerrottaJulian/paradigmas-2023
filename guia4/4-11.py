## Diseñar el algoritmo correspondiente a un programa, que:
## a) Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
## b) Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
## c) Muestra el contenido de la tabla en pantalla.


#carpetas

#desarrollo
diagonal = [];
for i in range (5):
  
  fila = [0 for i in range (5)];
  fila[i] = 1
  diagonal.append(fila);
  

print(diagonal);

for fila in diagonal:
  print(fila)