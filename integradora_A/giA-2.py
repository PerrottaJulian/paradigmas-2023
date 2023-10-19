"""
Suponiendo que el primer día del año fue lunes, 
escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. 
Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'
"""
import time

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

def diaSemana (dia):
    temp = 0
    for i in range (dia):
        try:
            dia_de_la_semana = dias_semana[temp]
        except:
            temp = 0
            dia_de_la_semana = dias_semana[temp]
        temp +=1        
    return dia_de_la_semana

dia = int(input("Dia del año: "))
print(diaSemana(dia))