"""
Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, 
calcule y retorne la nueva fecha en tres parámetros 
año (AAAA), mes (MM) y día (DD) que resulte de incrementar al parámetro fecha con el parámetro cantidad de días.
"""

#modulos
def separarFecha(fecha_simple):
    fecha_simple = str(fecha_simple)
    año = fecha_simple[:4]
    mes = fecha_simple[4:6]
    dia = fecha_simple[6:]

    fecha_ordenada = {"año": int(año), "mes": int(mes), "dia": int(dia)}
    return fecha_ordenada

def sumarDias(fecha, dias):
    for i in range (dias):
        fecha["dia"] = fecha["dia"]+1
        if fecha["dia"] > 30:
            fecha["dia"] = 1
            fecha["mes"] = fecha["mes"]+1

        if fecha["mes"] > 12:
            fecha["mes"] = 1
            fecha["año"] = fecha["año"]+1  

    return fecha
#variables
fecha = 0

#codigo principal
"""
while len(fecha != 8):
    try:
        fecha = int(input("Ingrese fecha (AAAAMMDD): "))
        if len(fecha != 8):
            print("ERROR: fecha en formato incorrecto")
    except:
        print("ERROR: la fecha tiene que ser un numero")
"""

fecha = 20021227
fecha_ordenada = separarFecha(fecha)
print(f"Fecha actual: {fecha_ordenada}")

print( f"Nueva fecha:  {sumarDias( fecha_ordenada, 5 )}  " )