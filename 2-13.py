## Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.Por cada habitantes se ingresa: sexo(M/F)y edad. La carga de datos analiza al ingresar cualquier otro valor para sexo. El programa debe informar:
## Aqué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.


#carpetas
import time;

#variables
cantidad_habitantes = int();
sexo = str();
edad = int();
cantidad_M = int();
cantidad_F = int();
hombre_mayor80 = bool();
mujeres_edadescolar = int();

cantidad_habitantes = 0;
sexo = "";
edad = 0;
cantidad_M = 0;
cantidad_F = 0;
hombre_mayor80 = False;
mujeres_edadescolar = 0;

#desarrollo

cantidad_habitantes = int(input("Ingrese cantudad de habitante de la poblacion: "));

for i in range(cantidad_habitantes):
    sexo = str(input("Sexo(M/F): "));
    sexo = sexo.upper();
    edad = int(input("Edad: "));


    if (sexo == "M"):
        cantidad_M += 1;

        if (edad > 80):
            hombre_mayor80 = True;

    elif (sexo == "F"):
        cantidad_F += 1;

        if (edad >= 4 and edad <= 18):
            mujeres_edadescolar += 1;

    time.sleep(0.4);


if (cantidad_M > cantidad_F):
    print("Hay mas hombres que mujeres.");
elif (cantidad_F > cantidad_M):
    print("Hay mas mujeres que hombres.");
else:
    print("Hay la misma cantidad de hombres y mujeres.");

print("Cantidad de mujeres en edad escolar:", mujeres_edadescolar);

if (hombre_mayor80 == True):
    print("Hay almenos un hombre mayor a 80 años.");
else:
    print("No hay ningun hombre mayor a 80 años.");










