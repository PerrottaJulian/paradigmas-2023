# Escribir funciones que resuelvan los siguientes problemas: 
# a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400. 
# b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
# c) Dada una fecha (día, mes, año), indicar si es válida o no. 
# d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
# e) Dada una fecha, indicar los días que faltan hasta fin de año. 
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. 
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días

meses = ["enero", "febrero", "marzo","abril", "mayo", "junio", "julio","agosto","septiembre", "octubre","noviembre", "diciembre"];
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

def bisiesto(año): #a
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
def diaMes(mes, año): #b
    if bisiesto(año) == True:
        if mes == "febrero":
            return 29;
        else:
            return dias_meses[meses.index(mes)];
    else:
        return dias_meses[meses.index(mes)];

def fechaValida(dia, mes, año): #c
    if dia > diaMes(mes, año) or dia < 0:
        return False
    else:
        return True


def finDeMes(dia, mes, año): #d
    if fechaValida(dia, mes, año) == True:
        return diaMes(mes, año) - dia;

def finDeAño(dia, mes, año): #e
    finde_año = finDeMes(dia, mes, año);
    if mes != "diciembre":
        for dias in dias_meses[meses.index(mes) + 1 :]:
            finde_año += dias
    return finde_año

def diasTranscurridos (dia, mes, año): #f
    dias_transc = 0;
    for dias in dias_meses[: meses.index(mes) + 1]:
        dias_transc += dias;
    
    if bisiesto(año) == False:
        return dias_transc - finDeMes(dia, mes, año);
    else:
        return dias_transc - finDeMes(dia, mes, año) + 1;


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
    if año1 <= año2:
        entreaños = año2 - año1
        dias_totales = finDeAño(dia1, mes1, año1) + 365*(entreaños) - finDeAño(dia2, mes2, año2);
        print(f" Aproximadmente {conversorFecha(dias_totales)} ({dias_totales} dias exactamente) ")
    
    elif año1 >= año2:
        entreaños = año1 - año2
        dias_totales = finDeAño(dia2, mes2, año2) + 365*(entreaños) - finDeAño(dia1, mes1, año1);
        print(f" Aproximadmente {conversorFecha(dias_totales)} ({dias_totales} dias exactamente) ")

tiempo2fechas(7, "enero", 2022, 8, "junio", 2024) #Unicamente no supe como incluir la cantidad exacta de dias que tiene cada mes especifico en la conversion final(lo simplifique a 30), por eso aclaro el aproximado.