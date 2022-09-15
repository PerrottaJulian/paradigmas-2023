## Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
## a) Determinar y mostrar el nombre del ganador de la carrera.
## b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
## c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.


#variables
n_competidores = int();
nombre = str();
tiempo_segs = float();
tiempo_ganador = float();
ganador = str();
tiempo_record = float();
suma_tiempos = float();
tiempo_promedio = float();

bandera = bool();

n_competidores = 0;
nombre = "";
tiempo_segs = 0.0;
tiempo_ganador = 0.0;
ganador = "";
tiempo_record = 0.0;
suma_tiempos = 0.0;
tiempo_promedio = 0.0;

bandera = True;

#desarrollo
n_competidores = int(input("Final de la carrera de ciclismo. Ingrese la cantidad de cliclistas participantes: "));

for i in range (n_competidores):
    print("Nombre del cliclista numero", (i+1), end=": ");
    nombre = str(input(""));
    print("Tiempo del ciclista numero", (i+1),"(en segundos)", end=": ");
    tiempo_segs = float(input(""));
    suma_tiempos += tiempo_segs;

    #If que solo va a entrar una ves, para definir un valor inicial a tiempo_ganador y despues en el siguiente if empezar a comparar
    if (bandera == True):
        tiempo_ganador = tiempo_segs;
        nombre_ganador = nombre;
        bandera = False;
    #

    if (tiempo_segs < tiempo_ganador):
        tiempo_ganador = tiempo_segs;
        nombre_ganador = nombre;
        

tiempo_record = float(input("Ingrese tiempo record de la carrera (En segundos): "));
print("El cliclista ganador es", nombre_ganador.upper(), "con un tiempo de: ", tiempo_ganador, "segundos");

if (tiempo_ganador < tiempo_record):
    print(nombre_ganador, "Ha superado el tiempo record. ");
    tiempo_record = tiempo_ganador;
    print("El nuevo tiempo record de la competicion es:", tiempo_record, "segundos");
elif(tiempo_ganador > tiempo_record):
    print("El ganador no ha superado el tiempo record de:", tiempo_record, "segundos");
else:
    print(nombre_ganador, "a empatado el tiempo record de la competicion, casi!");

tiempo_promedio = suma_tiempos / n_competidores;
print ("El tiempo promedio de la carrera fue: ", tiempo_promedio);