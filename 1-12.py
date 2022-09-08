##Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

#constantes
ahormes = 0.10

#variables
suel = int();
ahorro = float();

suel = 0;
ahorro = 0.0;

mesesaño = ["enero", "febrero", "marzo","abril", "mayo", "junio", "julio","agosto","septiembre", "octubre","noviembre", "diciembre"];
#desarrollo
for c in range (12):
    print("Ingresá tu sueldo de",mesesaño[c], end=": $");
    suel = int(input(""))
    ahorro = ahorro + suel * ahormes;


print("Ahorro total de este año:", ahorro); 
