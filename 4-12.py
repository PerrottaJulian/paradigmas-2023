## Diseñar el algoritmo correspondiente a un programa, que: Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’. 
## Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
## Visualiza el contenido de la matriz en pantalla.



#desarrollo
marco = [];
for i in range(5):
    fila = [];
    if i == 0 or i == 4:
        fila = [1 for i in range (15)];
    else:
        fila = [1];
        fila.extend([0 for i in range (13)]);
        fila.append(1)
        
    marco.append(fila)

for fila in marco:
    print(fila)