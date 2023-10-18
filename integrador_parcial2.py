"""
Crear un programa para gestionar datos de los socios de un club, permitiendo:
-Cargar información de los socios en un diccionario para acceder por número de socio. 
    Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). 
    El programa debe iniciar con los datos de los socios fundadores ya cargados:
        Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
        Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
        Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
-Informar cantidad de socios del club.
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
-Imprimir el listado de socios completo
Utilizar estructuras de datos def y menues
"""
import time

#Modulos
def separarFecha(fecha):
    fecha = str(fecha)
    dia = fecha[:2]
    mes = fecha[2:4]
    año = fecha[4:]

    fecha_ordenada = {"año": año, "mes": mes, "dia": dia}
    return fecha_ordenada

def fechaOrdenada (fecha):
    return(f"{fecha['dia']}/{fecha['mes']}/{fecha['año']}")

def cargarSocio(lista, indice):
    socio = dict()
    print("------------------------------------------ ")
    socio["numero"] = indice
    nombre = input("Ingresar nombre completo del socio: ")
    socio["nombre"] = nombre
 
    fecha_ingreso = input("Ingrese fecha de ingreso (en formato ddmmaaaa): ")
    while len(fecha_ingreso) != 8 or not(fecha_ingreso.isdigit) :
        fecha_ingreso = int(input("Ingrese una fecha correcta: "))
    socio["ingreso"] = fechaOrdenada(separarFecha(fecha_ingreso))
    
    cuota_aldia = input("Tiene la cuota al dia? (s/n) ")
    if cuota_aldia == "s":
        cuota_aldia = True
    else:
        cuota_aldia = False
    socio["cuotaAlDia"] = cuota_aldia

    lista.append(socio)

def cargarDatos(lista):
    i = 4
    continuar = "s"

    while continuar == "s":
        cargarSocio(lista, i)
        i+=1
        continuar = input("Continuar? (s/n) ")
        time.sleep(1)

## modulos del menu
def registrarPagos(lista, numero):
    for socio in lista:
        if socio["numero"] == numero:
            socio["cuotaAlDia"] = True

def cambiarFechas(lista):
    for socio in lista:
        if socio["ingreso"] == "13/03/2018":
            socio["ingreso"] = "14/03/2018"

def eliminarSocio(lista, nombre):
    for socio in lista:
        if socio["nombre"] == nombre:
            lista.remove(socio)

def listadoDeSocios(lista):
    print("")
    for socio in lista:
        if socio["cuotaAlDia"] is True:
            cuota = "cuota al dia"
        else:
            cuota = "cuota atrasada"

        print(f'*Socio n°{socio["numero"]}: {socio["nombre"]}, ingresó: {socio["ingreso"]}, {cuota}')

def menu(lista, opcion):
    if opcion == 1:
        print(f"Cantidad de socios: {len(lista)}")

    elif opcion == 2:
        n_usuario = int(input("Numero de usuario: "))
        registrarPagos(lista, n_usuario)
        print("Pagos resitrados con exito!")

    elif opcion == 3:
        cambiarFechas(lista)
    elif opcion == 4:
        nombre = input("Nombre del socio: ")
        eliminarSocio(lista, nombre)
    elif opcion == 5:
        listadoDeSocios(lista)


#Codigo Principal
lista_socios = [
{
    "numero": 1,
    "nombre": "Amanda Núñez",
    "ingreso": "17/03/2009",
    "cuotaAlDia": True
},
{
    "numero": 2,
    "nombre": "Bárbara Molina",
    "ingreso": "17/03/2009",
    "cuotaAlDia": True
}, 
{
    "numero": 3,
    "nombre": "Lautaro Campos",
    "ingreso": "17/03/2009",
    "cuotaAlDia": True
}
]

cargarDatos(lista_socios)

opcion = 0
while opcion < 6:
    print("\n******************** MENU DE OPCIONES ********************")
    print("1- Ver cantidad de socios del club\n2- Regitrar cuotas pagadas de un socio (por numero)\n"+
          "3- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, al 14/03/2018\n"+
          "4- Dar de baja a un socio (por nombre)\n5- Imprimir el listado de socios completo\n6- Salir")
    
    opcion = int(input("Que opcion elige?: "))
    time.sleep(1)
    menu(lista_socios, opcion)
    time.sleep(2)