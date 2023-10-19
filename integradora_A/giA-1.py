"""
Escribir funciones que resuelvan los siguientes problemas: 
a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400. 
b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
c) Dada una fecha (día, mes, año), indicar si es válida o no. 
d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
e) Dada una fecha, indicar los días que faltan hasta fin de año. 
f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. 
g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días
"""
meses = ["enero", "febrero", "marzo","abril", "mayo", "junio", "julio","agosto","septiembre", "octubre","noviembre", "diciembre"];
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];


def bisiesto(año): #a
    if (año%4 == 0 and año%100 != 0) or (año%4 == 0 and año%100 == 0 and año%400 == 0):
        return True
    else:
        return False
            
def diasMes_año(mes, año): #b
    if bisiesto(año):
        if mes == "febrero":
            return 29;
        else:
            return dias_meses[meses.index(mes)];
    else:
        return dias_meses[meses.index(mes)];

def fechaValida(dia, mes, año): #c
    if dia > diasMes_año(mes, año) or dia < 0:
        return False
    else:
        return True


def finDeMes(dia, mes, año): #d
    if fechaValida(dia, mes, año) == True:
        return diasMes_año(mes, año) - dia;
    else:
        return "Fecha no valida"

def finDeAño(dia, mes, año): #e
    if bisiesto(año):
        finde_año = 366
    else:
        finde_año = 365

    index_mes = meses.index(mes)
    for dias in dias_meses[:index_mes]:
        finde_año -= dias
    
    finde_año -= dia

    if fechaValida(dia,mes,año):
        return finde_año
    else:
        return "Fecha invalida"

def diasTranscurridos (dia, mes, año): #f
    if fechaValida(dia,mes,año):
        return 365-finDeAño(dia, mes, año)
    else:
        return "Fecha invalida"


def conversorFecha (dias):
    meses = 0;
    años = 0;
    while dias > 365:
        años += 1;
        dias -= 365;
    while dias > 30:
        meses += 1;
        dias -= 30;
    return str(años) + "A " + str(meses) + "M " + str(dias) + "D "



def tiempo2fechas (dia1, mes1, año1, dia2, mes2, año2): #g 
    fecha1 = {"dia": dia1, "mes": mes1, "año": año1}
    fecha2 = {"dia": dia2, "mes": mes2, "año": año2}

    if año1 <= año2:
        entreaños = año2 - año1 -1
        dias_totales = finDeAño(dia1, mes1, año1) + 365*(entreaños) + diasTranscurridos(dia2, mes2, año2);
        return(f" Aproximadmente {conversorFecha(dias_totales)} ({dias_totales} dias exactamente) ")
    
    elif año1 >= año2:
        entreaños = año1 - año2
        dias_totales = finDeAño(dia2, mes2, año2) + 365*(entreaños) + diasTranscurridos(dia1, mes1, año1);
        return(f" Aproximadmente {conversorFecha(dias_totales)} ({dias_totales} dias exactamente) ")

#tiempo2fechas(7, "enero", 2022, 8, "junio", 2024) #Unicamente no supe como incluir la cantidad exacta de dias que tiene cada mes especifico en la conversion final(lo simplifique a 30), por eso aclaro el aproximado.

#print (bisiesto(2100))

#print(fechaValida(31,"abril",2013))

#print(finDeAño(32,"febrero", 2018))

#print(diasTranscurridos(29,"febrero", 2012))

print(tiempo2fechas(31,"diciembre", 2017, 1,"enero",2019))

