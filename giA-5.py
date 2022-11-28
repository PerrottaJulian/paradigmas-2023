## Se pide que implemente el procedimiento ReparandoLaNave(). Teniendo en cuenta que el marciano de la imagen debe llegar a su hogar con suficiente combustible, se pide que recorra el camino indicado, teniendo en cuenta que en el medio se puede encontrar con combustible, el cual, es representados por celdas Rojas y Negras. 
## El combustible podría estar en cualquier parte del camino. Si el combustible es Rojo, nuestro amigo el marciano se detendrá y dejará una mancha Verde en el lugar, debido a que encontró combustible de calidad, pero luego seguirá su camino. Si el combustible es Negro, podrá avanzar sin problemas. El camino tiene 5 celdas de ancho

from random import randint;
import time

def tabla(matriz):
    for elemento in matriz:
        print(elemento);

def genFila():
    fila = [];
    for i in range (5):
        n = randint(1, 3);
        if n == 1:
            celda = "blanco";
        elif n == 2:
            celda = "negro ";
        else:
            celda = " rojo ";
        fila.append(celda)
    return fila

def ReparandoLaNave(): #Lo mas cercano a lo que se pedia que se me ocurrio
    mapa = [];
    for i in range (4):
        fila = genFila();
        mapa.append(fila);
    tabla(mapa);
    time.sleep(2)

    for fila in mapa:
        mov_marciano = randint(0, 4);

        if fila[mov_marciano] == "negro ":
            temp = fila[mov_marciano]
            fila[mov_marciano] = "MARCIANO"

        if fila[mov_marciano] == " rojo ":
            temp = "VERDE"
            fila[mov_marciano] = "MARCIANO"

        if fila[mov_marciano] == "blanco":
            print("El marciano no encontro combustible")
            break

        time.sleep(2)
        print(" ")
        print(" ")
        tabla(mapa)

        fila[mov_marciano] = temp

ReparandoLaNave();