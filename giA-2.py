## Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

def diaSemana (num):
    semana = num // 7
    print (dias_semana[num - 7*semana - 1]);


dia = int(input("Dia del año: "))
diaSemana(dia)