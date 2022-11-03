## Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
## a) La temperatura media de cada día
## b) Los días con menos temperatura
## c) Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.



#variables 
media_temperaturas = [];
menor_temperaturas = [];
temperaturas_maximas = [];
temperaturas_coincidentes = [];

tmax = int();
tmin = int();
t_media = float();
menor_t = int();

tmax = 0;
tmin = 0;
t_media = 0.0;
menor_t = 999999;

#desarrollo
print("Se debe ingresar la temperatura minima y maxima de los ultimos 5 dias.");

for dia in range(1, 6):
    print("Temperatura MAXIMA del dia", dia, ":", end=" ");
    tmax = int(input());
    temperaturas_maximas.append(tmax);
    
    print("Temperatura MINIMA del dia", dia, ":", end=" ");
    tmin = int(input());

    while (tmin > tmax):
       tmin = int(input("Parece que hubo un error. Volver a ingresar temperatura: "));

    t_media += (tmax + tmin)/2;
    media_temperaturas.append(t_media);

    if (tmin < menor_t):
        menor_t = tmin;
        menor_temperaturas = [];

    if (tmin == menor_t):
        dia = "Dia " + str(dia);
        menor_temperaturas.append(dia);

print(temperaturas_maximas)

print("Temperatura media de cada dia:", media_temperaturas);
print("Dias con menor temperatura:", menor_temperaturas);

t_ingresada = int(input("Ingresar una temperatura deseada para comparar: "));
for dia in range(1, 6):
    if (t_ingresada == temperaturas_maximas[dia-1]):
        dia = "Dia " + str(dia);
        temperaturas_coincidentes.append(dia);

if ( len(temperaturas_coincidentes) == 0):
    print("La temperatura ingresada no coincide con ninguna temperatura maxima");
else:
    print("Dias en los que su temperatura maxima coincide con la temepratura ingresada:", temperaturas_coincidentes);


