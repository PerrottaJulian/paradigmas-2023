## Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. El dato que recibe es un longint con una fecha en formato aaaammdd.


#modulos
def cortarYConvertirEnInt (string, inicio, final):
    if len(string) == 8:
        return int(string[inicio : final])
    else:
        return 999

def cartelFecha (dia, mes, año):
    return dia + "/" + mes + "/" + año


def mayorA (n1, n2):
    return n1 > n2

#variables
fecha = str();
año = int();
mes = int();
dia = int();


#codigo principal
print("Ingresar una fecha en formato aaaammdd y se devolvera la fecha ordenada");

fecha = int(input("Fecha: "));
fecha = str(fecha);

año = cortarYConvertirEnInt(fecha, 0, 4)
mes = cortarYConvertirEnInt(fecha, 4, 6)
dia = cortarYConvertirEnInt(fecha, 6, len(fecha))


while len(fecha) != 8 or mes > 12 or mes < 0 or dia < 0 or dia > 31:
    fecha = int(input("Error. Volver a ingresar fecha: "));
    fecha = str(fecha);

    año = cortarYConvertirEnInt(fecha, 0, 4)
    mes = cortarYConvertirEnInt(fecha, 4, 6)
    dia = cortarYConvertirEnInt(fecha, 6, len(fecha))

print(cartelFecha(str(dia), str(mes), str(año)));