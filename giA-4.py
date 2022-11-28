## Se quiere generar el código de programación necesario para realizar la afinación de un piano. Para esto, el afinador posee un dispositivo que escucha la nota de cada tecla, la compara con una nota esperada, e indica si es correcta o no. 
## La nota escuchada en el piano será correcta si la celda que la representa tiene el mismo color que la celda que representa la nota esperada. Hay dos tipos de teclas, blancas y negras, por lo que hay dos formas de representar la nota, con una celda blanca (vacía) o negra. En el caso contrario, el dispositivo indicará que la nota del piano debe afinarse y esto se representará marcando la nota mediante una celda de color Rojo.
## Se le pide que implemente el procedimiento VerificarAfinacionDePiano() que indica con un casillero rojo aquellas teclas del piano que deben afinarse, para un piano de 88 teclas.

from random import randint


def generarNotas():
    piano = []
    for i in range (15): #Serian 88 pero no se aprecia bien el resultdo
        n = randint(1, 2);
        if n == 1:
            tecla = "negra";
        else:
            tecla = "blanca";
        piano.append(tecla);
    return piano

def tabla(matriz):
    for elemento in matriz:
        print(elemento);

def VerificarAfinacionDePiano(n, ne):
    tabla_afinador = [];
    afinador = [];
    for i in range (len(n)):
        if n[i] == ne[i]:
            afinador.append("     ");
        else:
            afinador.append(" ROJA ");
    tabla_afinador.append(n);
    tabla_afinador.append(ne);
    tabla_afinador.append(afinador);

    tabla(tabla_afinador);

nota_escuchada = generarNotas();
nota_esperada = generarNotas();

VerificarAfinacionDePiano(nota_escuchada, nota_esperada);
