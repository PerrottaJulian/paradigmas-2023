## En la facultad se cuenta con las materias aprobadas de un alumno de Ingenieria en Sistemas (55 en total), sobre varios vectores y/o matrices
## Por materia probada se tiene: Codigo de la materia, Nombre de la materia, Año al que pertenece(1 a 5), Año de aprobacion (2005 a 2009) y Nota
## Se pide un menu que permita:
## a) Listado ordenado de materia de las asignaturas correspondientes a un año de la carrera determinado
## b) Permitir la modificacion de la nota de una materia ingresando Nombre y Año al que pertenece
## c) Calcular el promedio de materias aprobadas en el año 2007 y 2008


#carpetas
import time
from random import randint;

#variables
op = int();

op = 0;
#modulos
def verificar(n, menor, mayor):
    if n >= menor and n <= mayor:
        return True
    else:
        return False

def ordenarNombre(nombre):
    nombre = nombre.lower();
    nombre = nombre.capitalize();
    return nombre;

def listadoAños (matriz):
    años = [1,2,3,4,5];
    for año in años:
        lista_año = [];
        for materia in matriz:
            if materia[2] == año:
                lista_año.append(materia[1]);
        print(f"Año {año}: {lista_año}");

def cambiarNota(matriz):
    nombre = str(input("Nombre de la materia que quiere modificar la nota: "));
    nombre = ordenarNombre(nombre);
    año = int(input("Año al que pertenece: "));
    for materia in matriz_materias:
        if materia[1] == nombre and materia[2] == año:
            nueva_nota = int(input("Ingrese la nueva nota: "));
            materia[4] = nueva_nota;

def promedio20072008 (matriz):
    suma_materias = 0;
    cont_suma = 0;
    for materia in matriz:
        if materia[3] == 2007 or materia[3] == 2008:
            suma_materias += materia[4];
            cont_suma += 1;
    print(f"Promedio = {suma_materias/cont_suma}")

def menu(opcion):
    if opcion == 1:
        time.sleep(1);
        return listadoAños(matriz_materias);

    elif opcion == 2:
        time.sleep(1);
        return cambiarNota(matriz_materias)

    elif opcion == 3:
        time.sleep(1);
        return promedio20072008(matriz_materias);
        
#codigo principal
matriz_materias = []
for i in range (5): #se cambia a 55 pero uso menos para probar con facilidad. 
    #Tambien puse que los valores de la variables se generen por randint pero deje el codigo de verdad como comentario
    
    c_m = -1;
    n_m = "";
    a_m = -1;
    aa_m = -1;
    nota = -1;
    materia = []; 
    
#    while verificar(c_m, 0, 9999) == False:
#       c_m = int(input("Codigo de la materia (4 digitos): "));
    c_m = randint(0, 999)

    n_m = str(input("Nombre de la materia: "));
    n_m = ordenarNombre(n_m);

#    while verificar(a_m, 1, 5) == False:
#        a_m = int(input(f"Año al que pertenece {n_m}: "));
    a_m = randint(1, 5)
#    while verificar(aa_m, 2005, 2009) == False:
#        aa_m = int(input(f"Año de aprobacion de {n_m}: "));
    aa_m = randint(2005, 2009)
#    while verificar(nota, 4, 10) == False:
#        nota = int(input("Nota: "));
    nota = randint(4, 10)

    materia.extend([c_m, n_m, a_m, aa_m, nota]);
    matriz_materias.append(materia);
    time.sleep(1);

print(matriz_materias)   


while op != 4:
    op = 0;
    
    print( """
    1) Listado de materias por año
    2) Modificar Nota
    3) Promedio de materias aprobadas en los años 2007 y 2008
    4) Salir   """)

    while verificar(op, 1, 4) == False:
        op = int(input("Que opcion elige?: "));
        time.sleep(1);
        
    menu(op);