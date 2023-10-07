## Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
## - Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
## - Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
## El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
## ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

#2023

goles = -1
#carpetas
import time;

#desarrollo
partidos = [];
resultados = [];

print("Ingresar los equipos y el resultado del partido respectivo.");

for i in range (3):
    partido = [];
    resultado_partido = [];

    for i in range (2):
        goles = -1
        equipo = str(input(f"Equipo {i+1} : "));
        equipo = equipo.capitalize();

        while goles < 0:
            try:
                goles = int(input("Goles: "));
            except:
                continue

        partido.append(equipo);
        resultado_partido.append(goles);
    
    partidos.append(partido);
    resultados.append(resultado_partido);

quinela = []
for partido, resultado in zip(partidos, resultados):
    quinela.append(f"{partido[0]} {resultado[0]}-{resultado[1]} {partido[1]}")

for partido in quinela:
    print(partido);

