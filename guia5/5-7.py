"""
Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. 
El dato que recibe es un longint con una fecha en formato aaaammdd.
"""

#modulos
def separarFecha(fecha):
    fecha = str(fecha)
    año = fecha[:4]
    mes = fecha[4:6]
    dia = fecha[6:]

    fecha_ordenada = {"año": año, "mes": mes, "dia": dia}
    return fecha_ordenada

def mostrarFecha (fecha):
    print(f"{fecha['dia']}/{fecha['mes']}/{fecha['año']}")

#variables
mifecha = 0

#codigo principal
print("Ingresar una fecha en formato aaaammdd y se devolvera la fecha ordenada");

while len( str(mifecha) ) != 8:
    try:
        mifecha = int(input("Fecha: "))
        if len( str(mifecha) ) != 8:
            print("Ingrese una fecha correcta")
    except:
        print("Ingrese una fecha correcta")
        continue
            

mifecha_ordenada = separarFecha(mifecha)

mostrarFecha(mifecha_ordenada)
