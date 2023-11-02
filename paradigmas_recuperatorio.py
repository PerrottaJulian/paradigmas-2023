"""
En la facultad se cuenta con las materias aprobadas de un alumno de Ingenieria en Sistemas (55 en total), sobre varios vectores y/o matrices
Por materia probada se tiene: Codigo de la materia, Nombre de la materia, Año al que pertenece(1 a 5), Año de aprobacion (2005 a 2009) y Nota
Se pide un menu que permita:
a) Listado ordenado de materia de las asignaturas correspondientes a un año de la carrera determinado
b) Permitir la modificacion de la nota de una materia ingresando Nombre y Año al que pertenece
c) Calcular el promedio de materias aprobadas en el año 2007 y 2008
"""
#!2023


#* carpetas
import time

#* modulos
def esperar():
    time.sleep(0.5)
    print("...", end="")
    time.sleep(1)
    print("...")
    time.sleep(1)
  
def definirIntEntre (piso, techo, nombre):
    n = -999999
    while n < piso or n > techo:
        try:
            n = int(input(f"{nombre}: "))
            if n < piso or n > techo:
                print("Error: Ingreso de datos incorrecto")
        except:
            print("Error: Ingreso de datos incorrecto")
            continue
    return n

def Ingreso_de_datos():
    materias = list()
    for i in range(3):
        materia = dict()
        
        codigo = i+1
        materia["codigo"] = codigo

        nombre = input(f"Nombre de la materia {codigo}: ") 
        materia["nombre"] = nombre
        
        año = definirIntEntre (1, 5, "año")
        materia["año"] = año
        
        año_aprobacion = definirIntEntre(2005, 2009, "año de aprobacion")
        materia["año de aprobacion"] = año_aprobacion
        
        nota = definirIntEntre (4, 10, "nota")
        materia["nota"] = nota
         
        materias.append(materia)
        esperar()
        
    return materias

def listadoDeMaterias(lista_materias):
    for materia in lista_materias:
        for kw,val in materia.items():
            print(f"{kw}: {val}")
        print("---------------------------------------------")

def materiasPorAño(lista_materias, año):
    materias_por_año = list()
    for materia in lista_materias:
        if materia["año"] == año:
            materias_por_año.append(materia)
    return materias_por_año

def modificarNota(lista_materias, nombre, año, nueva_nota):
    for materia in lista_materias:
        if materia["nombre"] == nombre and materia["año"] == año:
            materia["nota"] = nueva_nota

def promedioEntre2007y2008(lista_materias):
    suma = 0
    contador = 0
    for materia in lista_materias:
        if materia["año de aprobacion"] == 2007 or materia["año de aprobacion"] == 2008:
            suma += materia["nota"]
            contador += 1
    return suma/contador      

def menu(materias, opc):
    if opc == 1:
        esperar()
        año = int(input("Segun que año quiere el elistado de materias?: "))
        materias_por_año = materiasPorAño(materias, año)
        listadoDeMaterias(materias_por_año)
        
    elif opc == 2:
        esperar()
        nombre = input("Nombre: ")
        año = definirIntEntre (1, 5, "año")
        nueva_nota = definirIntEntre (4, 10, "Nueva nota")
        
        modificarNota(materias, nombre, año, nueva_nota)    
    elif opc == 3:
        prom = promedioEntre2007y2008(materias)
        print(f"El promedio (2007-2008) es: {prom}")
    
#* codigo principal
#const
menu_str = "\n********** Menu **********\n1-Listado de asignaturas correspondientes a un año determinado\n2-Modificar nota de una materia(segun Nombre y Año)\n3-promedio de materias aprobadas en el año 2007 y 2008\n4-Salir"

#variables
opc = 0

#desarrollo
materias = Ingreso_de_datos()
#? listadoDeMaterias(materias)

while opc != 4:
    print(menu_str)
    opc = definirIntEntre(1, 4, "Que opcion elije? ")
    menu(materias, opc)
    esperar()
    
    
"""print(listadoDeMaterias(materias))

materias[0]["nota"] = 9

print("*************************************************************************")
print(listadoDeMaterias(materias))"""


    
    