##Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario.
##Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
##La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.


#constantes
diurno = 35.50;
noct = 40.60;

#variables
turno = int();
horas = int();
jornal = float();

turno = 0;
horas = 0;
jornal = 0.0;

#desarrollo
turno = int(input("Turno del operario este dia. 1 para DIURNO. 2 para NOCTURNO: "));

while (turno < 1 or turno > 2):
    print("ERROR.");
    turno = int(input("ingrese 1 o 2: "));

if (turno == 1):
    horas = int(input("Horas trabajadas esta jornada: "));
    jornal = horas * diurno;
    print ("jornal = $", jornal);
elif (turno == 2):
    horas = int(input("Horas trabajadas esta jornada: "));
    jornal = horas * noct;
    print ("jornal = $", jornal);
