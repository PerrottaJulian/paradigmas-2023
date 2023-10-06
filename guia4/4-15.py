## Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
## - Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
## - Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
## El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
## ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?



#carpetas
import time;

#variables
seguir = str();
equipo = str();
goles = int();

seguir = "";
equipo = "";
goles = int();

#desarrollo
equipos = [];
resultados = [];
quiniela = [];

print("Ingresar los equipos y el resultado del partido respectivo.");

while (seguir != "N"):
    partido = [];
    resultado_partido = [];

    for i in range (2):
        print("Equipo", i+1, ":", end=" ");
        equipo = str(input());
        equipo.capitalize();

        goles = int(input("Goles: "));

        partido.append(equipo);
        resultado_partido.append(goles);
    
    equipos.append(partido);
    resultados.append(resultado_partido);

    seguir = str(input("Continuar?(S/N): "));
    seguir = seguir.upper();


if len(equipos) == len(resultados):
    for partido in equipos:
        partido_resultado = [];
        
        partido_resultado = [partido[0] + "-" + partido[1] + ": " + str(resultados[equipos.index(partido)][0]) + "-" +str(resultados[equipos.index(partido)][1]) ];
        quiniela.append(partido_resultado);

for partido_resultado in quiniela:
    print(partido_resultado);

