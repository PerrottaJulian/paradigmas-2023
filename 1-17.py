## Galería de Arte. Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado.
## El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.

#constantes
año_act = 2022;

#variables 
año_cuadro1 = int();
año_cuadro2 = int();
año_cuadro3 = int();


año_cuadro1 = 0;
año_cuadro2 = 0;
año_cuadro3 = 0;

#desarrollo
print("Ingrese la fecha de creacion de los 3 cuadros.")
año_cuadro1 = int(input("1er cuadro: "));
año_cuadro2 = int(input("2do cuadro: "));
año_cuadro3 = int(input("3er cuadro: "));

if (año_cuadro1 < 1901 and año_cuadro2 < 1901 and año_cuadro3 < 1901):
    print("Todos los cuadros son anteriores al siglo XX");
else:
    if (año_cuadro1 < año_act and año_cuadro1 > (año_act - 10)):
        print("El primer cuadro tiene menos de 10 años de antiguedad.");

    if (año_cuadro2 < año_act and año_cuadro2 > (año_act - 10)):
        print("El segundo cuadro tiene menos de 10 años de antiguedad.");

    if (año_cuadro3 < año_act and año_cuadro3 > (año_act - 10)):
        print("El tercer cuadro tiene menos de 10 años de antiguedad.");
    
    if (año_cuadro1 < (año_act - 10) and año_cuadro2 < (año_act - 10) and año_cuadro3 < (año_act - 10)):
        print("RENOVAR STOCK")



