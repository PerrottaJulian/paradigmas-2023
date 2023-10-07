#Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.

#variables
base = float();
alt = float();

base = 0.0;
alt = 0.0;

#desarrollo
base = int(input("Ingrese la base del triangulo. Se le devolvera el area del mismo: "));
alt = base**2;

area = (base * alt) / 2;

print("El area del triangulo es: ", area);