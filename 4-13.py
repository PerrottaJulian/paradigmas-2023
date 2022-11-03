## De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana. Para guardar esta información se van a utilizar dos arreglos:
## - Nombre: Lista para guardar los nombres de los conductores.
## - kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
## Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor. Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.


#carpetas
import time;

#constantes
semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"];

#variables
conductor = str();
km = int();


conductor = "";
km = 0;

#desarrollo
nombres = [];
kms = [];
total_kms = [];

print("Debera ingresar el nombre del conductor y sus respectivos km que recorre cada dia de la semana. Para finalizar la carga de nombres, ingresar un asterisco(*).");
conductor = str(input("Conductor: "));
while (conductor != "*"):
    conductor = conductor.capitalize();
    nombres.append(conductor);

    kms_semana = [];
    for dia in semana:
        
        print("kilomestros conducidos el", dia, ":", end=" ")
        km = int(input());
        kms_semana.append(km);

    kms.append(kms_semana);
    time.sleep(1);
    conductor = str(input("Conductor: "));


for conductor in kms:
    suma_km = int();
    suma_km = 0;
    for km in conductor:
        suma_km += km;
    total_kms.append(nombres[kms.index(conductor)] + ": " + str(suma_km) + " kilometros")

print(total_kms);