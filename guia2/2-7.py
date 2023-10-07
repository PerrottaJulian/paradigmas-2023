## Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:cantidad de espectadores y descuento(S/N).La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:
## Calcular la recaudación total del complejo,considerando que el valor de la entrada e sde$50en los días con descuento y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones.


#constantes
si_descuento = 50;
no_descuento = 75;

#variables
cant_espectadores = int();
descuento = str();
total = int();
funciones_con_descuento = int();
funciones_totales = int();

cant_espectadores = 1;
descuento = "";
total = 0;
funciones_con_descuento = 0;
funciones_totales = 0;

#desarrollo

while (cant_espectadores != 0):
    cant_espectadores = int(input("Cantidad de espectadores: "));
    if (cant_espectadores == 0):
        break;
        
    descuento = str(input("Es dia de descuento? (S para si y N para no): "));

    while (descuento != "S" and descuento != "N"):
        print ("Error. pruebe devuelta")
        descuento = str(input("Es dia de descuento? (S para si y N para no): "));

    if (descuento == "S"):
        total += si_descuento * cant_espectadores;
        funciones_con_descuento += 1;
        funciones_totales += 1;
    
    elif (descuento == "N"):
        total += no_descuento * cant_espectadores;
        funciones_totales += 1;


print("Recaudacion total: ", total);
print("Funciones con descuento efectuadas: ", funciones_con_descuento);
print("El porcentaje de funciones con descuento es: ", funciones_con_descuento * 100 / funciones_totales);



