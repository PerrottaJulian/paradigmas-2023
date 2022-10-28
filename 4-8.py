## Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).

#carpetas
import time;

#variables
mayores_de_edad = [];
mas_grandes = [];

nombre = str();
edad = int();
edad_mayor = int();

nombre = "";
edad = 0;
edad_mayor = 0;

#desarrollo
print("""Debera ingresar el nombre y edad de cada alumno. La carga de datos finaliza al ingresar "*" en el nombre  """);

nombre = str(input("Nombre: "));
nombre = nombre.capitalize();
if (nombre != "*"):
    edad = int(input("Edad: "));

while(nombre != "*"):

    if (edad >= 18):
        mayores_de_edad.append(nombre);
    
    if (edad > edad_mayor):
        edad_mayor = edad;
        mas_grandes = [];
    
    if (edad == edad_mayor):
        mas_grandes.append(nombre)

    nombre = str(input("Nombre: "));
    nombre = nombre.capitalize();
    if (nombre != "*"):
        edad = int(input("Edad: "));
    time.sleep(0.5);




print("Alumnos mayores de edad:", mayores_de_edad);
print("Alumnos mas grandes:", mas_grandes);