##Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
##a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
##b) Determinar en qué mes recibió el sueldo más bajo del período.
##c) Informar el sueldo promedio del semestre.

#variables
sueldo = int();
sueldo_mas_alto = int();
aguinaldo = float();
sueldo_mas_bajo = int();
mes_mas_bajo = str();
suma_sueldos = int();
sueldo_prom = float();

bandera = bool();

sueldo = 0;
sueldo_mas_alto = 0;
aguinaldo = 0.0;
sueldo_mas_bajo = 0;
mes_mas_bajo = ""
suma_sueldos = 0;
sueldo_prom = 0.0;

bandera = True;
primer_semestre = [];

#desarrollo
primer_semestre = ["enero", "febrero", "marzo","abril", "mayo", "junio"];
for i in range (6):
    print("Ingrese el sueldo de", primer_semestre[i], end=": $");
    sueldo = int(input(""));

    suma_sueldos += sueldo

    if (bandera == True):
        sueldo_mas_alto = sueldo;
        sueldo_mas_bajo = sueldo;
        mes_mas_bajo = primer_semestre[i];
        bandera = False;

    if (sueldo > sueldo_mas_alto):
        sueldo_mas_alto = sueldo;

    if (sueldo < sueldo_mas_bajo):
        sueldo_mas_bajo = sueldo;
        mes_mas_bajo = primer_semestre[i];
    
aguinaldo = sueldo_mas_alto/2;
print("Su aguinaldo de este semestre es de $", aguinaldo);

print("Recibio el sueldo mas bajo en el mes de", mes_mas_bajo);

sueldo_prom = suma_sueldos//6;
print("El sueldo promedio de este semestre es: $", sueldo_prom);
